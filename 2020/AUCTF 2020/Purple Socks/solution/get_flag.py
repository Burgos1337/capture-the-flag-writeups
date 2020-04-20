from z3 import *

seed = [0x61, 0x75, 0x63, 0x74, 0x66]
secret = [0xe, 0x5, 0x6, 0x1a, 0x39, 0x7d, 0x60, 0x75, 0x7b, 0x54, 0x18, 0x6a]

inp = [BitVec('a%d'%i, 8) for i in range(len(secret))]
res = [0 for _ in range(len(inp))]

for x in range(len(inp)):
    v5 = x % 5
    res[x] = inp[x] ^ seed[v5]
    seed[v5] = res[x]
    s.add(res[x] == secret[x])

if s.check() == sat:
    model = s.model()
    print(''.join([chr(int(str(model[inp[z]]))) for z in range(len(inp))]))
else:
    print("unsat")
