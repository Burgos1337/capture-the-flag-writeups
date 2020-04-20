from pwn import *
from functools import reduce

fib = lambda n:reduce(lambda x, n:[x[1], x[0] + x[1]], range(n), [0, 1])[0]

def debug(txt, res, n):
    log.info("Text {txt} rotated with key {n}  --> {res}")

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        result += chr((ord(text[i]) + s - 65) % 26 + 65)
    return result

con = remote("52.207.14.64", 20300)
aa = 0
for i in range(6):
    con.recvline()
for x in range(50):
    line = con.recvline().decode().split(' ')
    if (aa > 0):
        line = line[1:]
    print (line)
    txt = line[1]
    nbr = int(line[3].split('=')[1])
    res = encrypt(txt, fib(nbr))
    con.sendline(res)
    debug(txt, res, nbr)
    aa += 1

log.info(con.recvall())
