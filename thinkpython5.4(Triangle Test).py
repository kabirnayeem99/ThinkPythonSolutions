print("if any of the three lengths is greater than"),
print("the sum of two others this cannot be an triangle")

def is_triangle(a, b, c):
	if a + b == c or b + c == a or c + a == b:
		print("Yes")
	else:
		print("No")

a = float(input("The value of the first lengths:"))
b = float(input("The value of the second lengths:"))
c = float(input("The value of the third lengths:"))

is_triangle(a, b, c)
