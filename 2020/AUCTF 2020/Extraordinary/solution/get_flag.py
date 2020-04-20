from pwn import *
from string import *

host = 'challenges.auctf.com'
port = 30030
p = remote(host, port)

uppercase = '{ABCDEFGHIJKLMNOPQRSTUVWXYZ_-}'
lowercase = '{abcdefghijklmnopqrstuvwxyz_-}' + digits
find = ''

try:
    while True:
        for ch in lowercase[::-1]:
            data = find + ch
            p.sendline(data)
            msg = p.recvuntil("'\n").split()[1][2:-1]
            print(data, '->', msg)
            if len(msg) == 0:
                find += ch
                print('Good :', find)
except KeyboardInterrupt:
    print(find)
