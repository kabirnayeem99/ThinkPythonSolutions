def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print("Sir, \nYou are done with counting!")

n = int(input("Where to start? \n"))
print("Your assigned number is ", n)
#countdown(n)

def sequence(n):
    while n != 1:
        print("The processed number is", n,)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
sequence(n)
