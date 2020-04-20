import struct
import sys
from PIL import Image

if len(sys.argv) != 2:
	print("[+] Usage : ./{sys.argv[0]} <filename>")
	exit(1)

with open(sys.argv[1] , "rb") as f:
	data = f.read()

assert data[:4] == b'PNG2'

width = struct.unpack(">H" , data[10:12])[0]
height = struct.unpack(">H" , data[19:21])[0]

img = Image.frombytes("RGB" , (width , height) , data[21:])
img.save("check.png" , "PNG")
