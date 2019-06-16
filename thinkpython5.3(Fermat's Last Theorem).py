
def check_fermat(a, b, c, n):
	if n > 2:
		if a ** n + b ** n == c ** n:
			print("Holy smoke, the Fermat was wrong!")
		else:
			print("No that doesn't work")
	else:
		print("Your value is less than 2")	

a = int(input("The value of a: "))
b = int(input("The value of b: "))
c = int(input("The value of c: "))
n = int(input("The value of n: "))

check_fermat(a, b, c, n)
