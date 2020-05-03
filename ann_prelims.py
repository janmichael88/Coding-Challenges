import numpy as np 

w = np.array([0,0])
b = 0
x1 = np.array([-1,1])
x2 = np.array([0,-1])
x3 = np.array([10,1])

y1 = 1
y2 = -1
y3 = 1

xs = [x1,x2,x3]
ys = [y1,y2,y3]


for i in range(0,len(xs)):
	if (ys[i]*np.dot(xs[i],w) + b) <= 0:
		#update weight and bias
		w = w + np.dot(xs[i],ys[i])
		b = b + ys[i]
		print(w)
	else:
		continue

print(np.sum(w)+b)



import numpy as np 

def grad(w1,w2):
	return(.5*(w1**2 + w2**2))

eta = 0.01

w = [1,0]

for i in range(100):
	#calculate gradient
	w = np.array(w) - np.array(eta*grad(w[0],w[1]))
	#get new gradient
	gradient = grad(w[0],w[1])
	print(gradient)





vals = []

def f1(n):
	return(2**n)

for i in range(32):
	vals.append(f1(i))
print(sum(vals))

import numpy as np 
print(0.5*np.log(1-10**(-6)))

import numpy as np 
A = np.array([[0,1],[2,3]])
B = np.array([[1,-1],[1,0]])

print(np.multiply(A,B).sum())


############## 
#RNNS
#
import numpy as np

h_0 = np.array([[1,0],
	[1,1]])
x_1 = np.array([[1,0],
	[2,1]])
x_2 = np.array([[3, -1],
	[4,0]])

h_2 = np.matmul(np.transpose(np.matmul(np.transpose(h_0),x_1)),x_2)
print(h_2)

import numpy as np

W_hh = np.array([[0.5,1],
	[1,2]])

W_hx = np.array([[1,0],
	[-1,0]])

W_hy = np.array([[-1,1],
	[1,2]])

h_0 = np.array([1,1])
x_1 = np.array([4,4])



h_1 = np.tanh(np.dot(W_hh,h_0) + np.dot(W_hx,x_1))

y_1 = np.dot(W_hy,h_1)

print(y_1)


import numpy as np 

C_tminus1 = np.array([0.5,0,0.3])
i_t = np.array([0.2,0.5,0.5])
Ct = np.array([0.5,0.6,0.4])

a = C_tminus1 + np.multiply(i_t,Ct)

print(a)


import numpy as np
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

W = np.array([[1,2],
			[0,-1],
			[2,1]])

b = np.array([-2,3])

v = np.array([1,-2,0])
print(W[:,0].shape, v.shape)

print(sigmoid(b[0] + np.dot(W[:,0],v)))






