# -*- coding: utf-8 -*-
"""
Created for Spring 2020 CTF
350 Points
Welcome to the AES-CTR oracle!
Our oracle's function is AES-GCM.
Our oracle has a consistent header.
The oracle is found at umbccd.io:13376, and your methods are:
    flg - returns the 16 byte nonce followed by the encrypted and authenticated flag
    enc - returns the encryption of the message after the : in "enc:..." with
          the first 16 bytes interpreted to be the nonce, which is represented
          as a 16 byte nonce followed by the authenticated ciphertext (16b tag)
    dec - returns the decryption of the authenticated ciphertext after the : in 
          "dec:<16 byte nonce>..." as a bytes string.
          
@author: pleoxconfusa
"""

import socket
from string import printable

BLOCK_SIZE = 16
pad = lambda s: s + ((BLOCK_SIZE - len(s) % BLOCK_SIZE) % BLOCK_SIZE) * b'\0'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('crypto.ctf.umbccd.io', 13376)
sock.connect(server_address)

msg = 'flg'.encode()
sock.sendall(msg)
ct = sock.recv(1024)
print(ct)

nonce = ct[:16]

encflag = ct[16:]

pt = "DawgCTF{".encode()

msg = b'enc:' + nonce + pt
sock.sendall(msg)
enc = sock.recv(1024)
print(enc)
print(enc.encode('hex'))

print(ct.encode('hex'))
msg = b'dec:' + nonce + enc[:-1] + "\x11"
sock.sendall(msg)
dec = sock.recv(1024)
print(dec) 
    
sock.close()

flag = 'DawgCTF{'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('crypto.ctf.umbccd.io', 13376)
sock.connect(server_address)

msg = 'flg'.encode()
sock.sendall(msg)
ct = sock.recv(1024)
print(ct)

nonce = ct[:16]

encflag = ct[16:]

for bbb in range(len(encflag) - len(flag)):
    for i in printable:
	guess = i
	pt = flag + guess

        msg = b'enc:' + nonce + pt
	sock.sendall(msg)
	enc = sock.recv(1024)
	enc = enc[16:]

	if (enc[len(flag)] == encflag[len(flag)]):
	   print("FOUND!!")
	   flag += guess
	   print(flag)
	   break
