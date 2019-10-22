#write a function that returns the nth term of a finabcci sequence
def fib(n):
	if n ==1:
		return(1)
	elif n == 2:
		return(1)
	elif n > 2:
		#use function again
		return fib(n-1) + fib(n-2)

#usinf function again print the first 14 terms
#this function is slow
for j in range(0,20):
	print(j,":",fib(j))

#memoization
#create dictionary that will story histroy of n times used fib
fib_cache = {}
def fib1(n):
	#if we have cached the value, then return it
	if n in fib_cache:
		return(fib_cache[n])
	#copmute the N'th term otherwuse
	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fib1(n-1) + fib1(n-2)
	#cache the value then return it
	fib_cache[n] = value
	return(value)


for num in range(1,150):
	print(num, ":", fib1(num))

#much faster
#add in edge cases
from functools import lru_cache
@lru_cache(maxsize = 10000)
def fib2(n):
	#first check that in is postive integer
	if type(n) != int:
		raise TypeError("n must be a postive int")
	#check to see if n less than 1
	if n < 1:
		raise ValueError("n must be a postive int")
	if n == 1:
		return(1)
	elif n == 2:
		return(1)
	elif n > 2:
		return(fib2(n-1)+fib2(n-2))


#now get the ratio between conse terms
for n in range(1, 60):
	print('ratio is', fib2(n+1)/fib2(n))		

#test the function 
for num in range(0,2000):
	print(num,':' ,fib2(num))















