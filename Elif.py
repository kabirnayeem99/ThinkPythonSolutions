x = int(input())
y = int(input())
sum = x + y
Zero = sum - x
Zero2 = sum - y
if sum == Zero:
    print("Y is 0")
elif sum == Zero2:
    print("X is 0")
elif sum != Zero and sum != Zero2:
    print("Neither is 0")


