def is_palindrome(word, wordr):
    if wordr == wordr[::-1]:
        print(word, "is a palindrome.")
    else:
        print(word, "is not a palindrome.")

word = input("give us a word to check: ")
wordr = word.lower()
is_palindrome(word, wordr)

#print("It is palindrome" if word == word[::-1])
