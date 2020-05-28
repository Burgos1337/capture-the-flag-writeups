#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from secret import FLAG


for i in range(1, 6):
    with open('{}.pub.pem'.format(i), 'rb') as f:
        key = RSA.importKey(f.read())
    with open('{}.enc'.format(i), 'wb') as f:
        f.write(key.encrypt(FLAG.encode(), None)[0])
