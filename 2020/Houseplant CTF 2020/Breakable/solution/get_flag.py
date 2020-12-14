seed_string = 'k33p_1t_in_pl41n'

result = '\xd2\x92\x64\xdd\xbe\xa4\xa4\xbe\xd9\xe0\x8f\xe5\xd0\x93\x63\xdd\xc6\x90\xa5\xcc\xc8\xe1\x8f\xcf\xdc\xa6\x61\xe3'

solution_onwards = ''

for i in range(14):
    solution_onwards += chr(ord(result[i]) - ord(seed_string[i]))

solution_before = ''

for i in range(14):
    solution_before += chr(ord(result[i + 14]) - ord(seed_string[i + 2]))

print('final', 'rtcp{' + solution_before + solution_onwards[-2:] + '}')
