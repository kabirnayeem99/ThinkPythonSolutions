def has_no_e(essay):
    wordful = essay.strip()
    for word in essay:
        for letter in word:
            if letter == 'e':
                print("This word has an e")
            else:
                print("No E")


#essay = input()
#essay = open(essay)
essay = open('/home/kabir/docs/python/mywork/no_e.txt')
has_no_e(essay)
print(essay.strip())
