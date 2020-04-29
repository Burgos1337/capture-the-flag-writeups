from z3 import *

def algo(inp):
	got = "ow0_wh4t_4_h4ckr_y0u_4r3"

	realflag = [9, 4, 23, 8, 17, 1, 18, 0, 13, 7, 2, 20, 16, 10, 22, 12, 19, 6, 15, 21, 3, 14, 5, 11]
	therealflag = [20, 16, 12, 9, 6, 15, 21, 3, 18, 0, 13, 7, 1, 4, 23, 8, 17, 2, 10, 22, 19, 11, 14, 5]

	theflags = ['*'] * 24
	theflags0 = ['*'] * 24
	theflags1 = ['*'] * 24
	theflags2 = ['*'] * 24

	i = 0
	for x in realflag:
		theflags[x] = inp[i]
		i += 1
        
	i = 0
	for x in therealflag:
		theflags0[x] = ord(got[i])
		i += 1
        
	i = 0
	for x in therealflag:
		theflags1[x] = inp[i]
		i += 1

	theflag = []
	thefinalflag = []

	for i in range(21):
		theflag.append(theflags[i]) 
        
	for i in range(21, 24):
		theflag.append(theflags1[i]) 

	for p in range(24):
		thefinalflag.append((theflags0[p] + (theflag[p])))

	for p in range(24):
		thefinalflag[p] = \
			If ( And(thefinalflag[p] > 145, thefinalflag[p] < 157),
			thefinalflag[p] + 10, 
			thefinalflag[p]) 
	
	return thefinalflag



s = Solver()
inp = []
target = [157, 157, 236, 168, 160, 162, 171, 162, 165, 199, 169, 169, 160, 194, 235, 207, 227, 210, 157, 203, 227, 104, 212, 202]

for i in range(24):
	b = BitVec("%d" % i, 16)
	inp.append(b)

res = algo(inp)

for i in range(24):
	s.add((res[i]) == (target[i]))

s.add(inp[3] != 41)

while s.check() == sat:
	solution = s.model()
	block = []
	flag = ""
	for i in range(len(inp)):
		c = inp[i]
		try: 
			flag += (chr(int(str(solution[c])))) 
		except :
			pass
		block.append(c != solution[c])
	print(flag)