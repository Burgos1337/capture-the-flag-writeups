f = open('purple_socks', 'rb').read()

key = 78

dat = '' 

for i in f:
    try:
        sor = chr(ord(i) ^ key)
    except:
        sor = chr(i ^ key)
    if sor == 'N':
        dat += i
    else:
        dat += sor

with open('data', 'wb') as out:
    out.write(dat)
    out.close()
