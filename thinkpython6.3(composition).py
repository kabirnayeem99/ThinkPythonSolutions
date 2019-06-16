print("Write a function is_between(x, y, z) "),
print("That returns True if x <= y <= z or False.")

def is_between(x, y, z):
	if x <= y:
		if x <= z:
			print(True)
	else:
		print(False)

is_between(3, 4, 5)
