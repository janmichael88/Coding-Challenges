'''
A frog wants to cross a river that is 11 feet across.
There are 10 stones in a line leading across the river, separated by 1 foot, 
and the frog is only ever able to jump one foot forward to the next stone, 
or two feet forward to the stone after the next. 

In how many different ways can he jump exactly 11 feet to the other side of the river?
'''

'''
My notes:


First ask, how many ways can the frog jump in 11 jupmps
this is just 1,1,1,1,1,1,1,1,1,1 so thats 11 C 0



Now in 10 jupmps
2,1,1,1,1,1,1,1,1,1 this can happen 10 ways
or just 10C1

Now in 9 jumps
2,2,1,1,1,1,1,1,1
1,2,2,1,1,1,1,1,1

8+7+6+5+4+3+2+1



in 8 jumps
2,2,2,

in 7 jumps
2,2,2,2,1,1,1



shortest is
6 jumps
2,2,2,2,2,1 this can happen 6 ways




if we define f(n) = something
as n feet away how many jumps

for example 
f(1) = 1
since its one foot away

and f(2) = 2
since the frog can either jump 1 or two feet

one jump will bring it to n-1
two jumps will bring it to n-2

for n greater than 2, we can define a recursive relationship as
f(n) = f(n-1) + f(n-2)

which is just the fibonacci sequence


 
'''
import math
def count_ways(n,r):
	num = math.factorial(n)
	den = math.factorial(r)*math.factorial(n-r)
	return(num/den)



print(count_ways(n=9,r=2))



def fibonacci(n):
    if n < 0:
        raise ValueError("invalid index!")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))

#code binary search
def binary_search(A,item):
	'''
	A is an array, the item is what we want to search
	'''
	if len(A) == 0:
		return False
	else:
		middle = len(A) // 2
		if A[middle] == item:
			return(True)
		if item < A[middle]:
			return binary_search(A[middle], item)
		else:
			return

numbers = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
print(binary_search(numbers, 4))
print(binary_search(numbers, 42))


