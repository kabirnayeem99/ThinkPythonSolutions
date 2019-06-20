fin = open('/home/kabir/docs/python/mywork/words.txt')
for line in fin:
    word = line.strip()
    if len(word) >= 20:
         print(word)
