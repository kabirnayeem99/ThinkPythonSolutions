"just adding an comment to see how it goes with git"
import math

def sum(x, y, su):
    summed = x + y
    if summed == su:
        print("Right")
    else:
        print("Wrong")

def mul(x, y, su):
    summed = x * y
    if summed == su:
        print("Right")
    else:
        print("Wrong")

def min(x, y, su):
    summed = x - y
    if summed == x - y:
        print("Right")
    else:
        print("Wrong")

def dev(x, y, su):
    summed = x / y
    if summed == x / y:
        print("Right")
    else:
        print("Wrong")

def func(fun):
    if fun == "+":
        sum(x, y, su)
    if fun == "*":
        mul(x, y, su)
    if fun == "-":
        min(x, y, su)
    if fun == "/":
        dev(x, y, su)

fun = str(input("The function is:"))
x = float(input("Enter the first number:"))
y = float(input("Enter the second number:"))
su = float(input("The result is:"))


print(math.log10(10))
