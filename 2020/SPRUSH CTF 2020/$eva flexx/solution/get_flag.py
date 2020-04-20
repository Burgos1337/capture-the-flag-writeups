import requests
from itertools import islice
import os
from process_latex import process_sympy

s = requests.Session()

req = s.get("http://tasks.sprush.rocks:8084/")

for k in range(150):
   text = ""

   for symbol in req.text[666:]:
     if (symbol != '$'):
       text += symbol
     else:
       break

   print(text)
   text = str(process_sympy(text))
   print(text)
   text += "  "

   f = text.replace("Integral(", "").replace("left*", "").replace("right*", "").replace("right", "").replace("left", "").replace("exp*", "exp").replace("(x, 0, 10)", "").replace(", )", "").replace(", E)", ")")
   f = f.replace("expx**3", "exp(x**3").replace("expx**2", "exp(x**2)").replace("expx", "exp(x)")
   print(f)

   fp = open('seva.py', 'w')
   fp.write("import scipy.integrate\n")
   fp.write("from numpy import *\n")
   fp.write("f = lambda x:")
   fp.write(str(f))
   fp.write("\n")
   fp.write("i = scipy.integrate.quad(f, 0, 10)\n")
   fp.write("ans = int(round(i[0]))\n")
   fp.write("print(ans)\n")
   fp.close()
   os.system('python seva.py > seva.txt')
   with open('seva.txt') as seva:
      head = islice(seva, 1)
      line = str(list(head))
      answer = line[2 : len(line) - 4]
   print(answer)

   req = s.post("http://tasks.sprush.rocks:8084/", data = {'answer': answer})
   if ("SPR" not in req.text):
     print(req.text[571:574])
   else:
     print(req.text)