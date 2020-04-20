import scipy.integrate
from numpy import *
f = lambda x:(-(9*x**3 - 4*x**2 + x**2 + x**2 + 3*x**1) + 6*x**1 + 9*x**1)  
i = scipy.integrate.quad(f, 0, 10)
ans = int(round(i[0]))
print(ans)
