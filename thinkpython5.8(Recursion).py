import random
def countdown(x):
	if x <= 0:
		print("blastoff!!")
	else:
		print(x)
		countdown(x-1)
	return x

x = random.randint(4, 134)
print("The random value is", x),
print("Let the countdown begin"),
countdown(x)
