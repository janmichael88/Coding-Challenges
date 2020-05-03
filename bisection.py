import numpy as np 
def f1(a):
	return(a**2 -15)

def sign(x):
	return(1-(x<=0))

tol = .00001
end1 = 0
end2 = 40
NMAX = 10000

N = 1
while N <= NMAX:
	#calculate new mid point
	c = (end1 + end2) / 2
	if (f1(c) == 0) or ((end2 - end1) /2 < tol):
		print(c)
		break
	else:
		N += 1
		#update C
		if sign(f1(c)) == sign(f1(end1)):
			end1 = c
		else:
			end2 = c

