def egcd(a, b):
    if a == 0:
       return (b, 0, 1)
    else:
       g, y, x = egcd(b % a, a)
       return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
       raise Exception("Modular inverse doesn't exist")
    else:
       return x % m

output = ""

n = 960242069
e = 347
p = 151
q = 6359219
df = [346046109, 295161774, 616062960, 790750242, 259677897, 945606673, 321883599, 625021022, 731220302, 556994500, 118512782, 843462311, 321883599, 202294479, 725148418, 725148418, 636253020, 70699533, 475241234, 530533280, 860892522, 530533280, 657690757, 110489031, 271790171, 221180981, 221180981, 278854535, 202294479, 231979042, 725148418, 787183046, 346046109, 657690757, 530533280, 770057231, 271790171, 584652061, 405302860, 137112544, 137112544, 851931432, 118512782, 683778547, 616062960, 508395428, 271790171, 185391473, 923405109, 227720616, 563542899, 770121847, 185391473, 546341739, 851931432, 657690757, 851931432, 284629213, 289862692, 788320338, 770057231, 770121847]

for c in df:
    fi = (p - 1) * (q - 1)
    d = modinv(e, fi)
    output += ("%x" % pow(c, d, n)).decode("hex")

print(output)
