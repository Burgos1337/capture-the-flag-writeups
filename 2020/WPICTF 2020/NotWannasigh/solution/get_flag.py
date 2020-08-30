with open('flag-gif.EnCiPhErEd', 'rb') as f:
     x = [i for i in f.read()]

with open('key.txt', 'rb') as f:
     y = list(map(int, f.read().split()))

gif = []

for a, b in zip(x, y):
    gif.append(a ^ b)

with open('flag.gif', 'wb') as f:
     f.write(bytearray(gif))
