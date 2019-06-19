"""write  a function find to that will take three parameter --- a string, an index to know where to start and a letter to find it out."""
def find(word, ind, let):
    index = 0
    word = word[ind:len(word)]
    while index < len(word):
        if word[index] == let:
            print("The letter is located in", index + 1, "position.")
            return index
        index = index + 1
    return - 1
word = "umbrella"
ind = "1"
let = "a"
