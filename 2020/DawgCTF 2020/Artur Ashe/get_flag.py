from pwn import *

r = remote('arthurashe.ctf.umbccd.io', 8411)

r.recvuntil('[Y/n]?')

r.sendline('\n')

flag = ""

for i in range(700):
        ahi = r.recv(8192).strip()
        ahu = ahi.split(' ')
        payload = ahu[-1][:-1]

        if '-love' in payload:
                r.sendline('0')
                flag += "0"
                print(flag)
        elif 'love-' in payload:
                r.sendline('1')
                flag += "1"
                print(flag)
        elif 'set-' in payload:
                r.sendline('0')
                flag += "0"
                print(flag)
        elif '-set' in payload:
                r.sendline('1')
                flag += "1"
                print(flag)
        elif 'game-' in payload:
                r.sendline('0')
                flag += "0"
                print(flag)
        elif '-game' in payload:
                r.sendline('1')
                flag += "1"
                print(flag)
        else:
                pay = payload.split('-')
                try:
                  math = int(pay[0]) - int(pay[1])
                  if math < 0:
                        r.sendline('1')
                        flag += "0"
                        print(flag)
                  else:
                        r.sendline('0')
                        flag += "1"
                        print(flag)
                except:
                  pass

# Then decode the binary string and get the flag
