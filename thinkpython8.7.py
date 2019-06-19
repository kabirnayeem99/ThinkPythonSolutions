def in_both(sentence, sentence2):
    for leta in sentence:
        if leta in sentence2:
            print(leta)

sentence = input("Write here a sentence: ")
sentence2 = input("Write another one:")
let = input("The letter you want to count: ")
num_e = sentence.count(let)
print("There are ", num_e, let.upper(), "in the first sentence sentence.")
#some code goes to in operator
in_both(sentence, sentence2)
