def rotate_word(word, amount):
    for character in word:
        numc = ord(character) + amount
        print(chr(numc))
rotate_word("fruit", 3)
