""" I had to write a function that would take a string and would print out the
first, last the middle of this strings"""
def first(word):
    print("The first letter of this word is ", word[0])
    return word[0]
def middle(word):
    print("The middle part of this word is ", word[1: -1])
    return word[1: -1]
def last(word):
    print("And the last part of this word is ", word[-1])
    return word[-1]
def is_palindrome(word):
    if len(word) <= 1:
        print("... ... ... \n Yes, this one is a palindrome, brother.")
    if last(word) != first(word):
        print("... ... ... \n Alas!!! Brother, no, this one is not.")

    return is_palindrome(middle(word))

a = input("Please, tell us the magical word \n")
first(a)
middle(a)
last(a)
print("Now, give us some time to find out if your word is a palindorme. \n ... \n ... ... \n ... ... ...")
is_palindrome(a)
