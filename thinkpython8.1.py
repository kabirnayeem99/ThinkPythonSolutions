one_string = input("Give us a string: \n")
index = -1
index_mini = (-1) * (len(one_string))
"""Write a funciton that takes a string as an arguement and displays the letters backward, one per line"""
"""here we take the index as -1, as it would print the
last alphabet. then subtracting 1 each time and to print the
previous.
but, the rule is, it must be bigger than or equal to minus lenght of this sttring."""
while index >= index_mini:
    letter = one_string[index]
    print(letter)
    index = index - 1
