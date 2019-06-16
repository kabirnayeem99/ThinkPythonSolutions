import random 
def factorial(n):
	if n == 0:
		print(1)
	else:
		recurse = factorial(n-1)
		result = n * (recurse)
		print(result)

n = random.randint(5, 500)	
factorial(n)
