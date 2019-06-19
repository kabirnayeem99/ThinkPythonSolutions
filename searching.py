def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            print("And the letter you mentioned is located in" ,index + 1,"th position.")
            return index
        index = index + 1
    reuturn - 1
word = input("Give us your string: ")
letter = input("And the letter: ")
find(word, letter)
