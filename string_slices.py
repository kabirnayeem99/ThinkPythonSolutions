ostring = input(">>>Say something, my girl, just anything. \n>>>")
word1 = ostring[0]
word2 = ostring[2:6]
word3 = ostring[7:10]

if word1 == "I" and word2 == "love" and word3 == "you":
    print(">>>Yes!!! She loves you")
    ostring = input(">>>Can you say that again, plese??? \n>>>")
    word1 = ostring[0]
    word2 = ostring[2:6]
    word3 = ostring[7:10]
    if word1 == "I" and word2 == "love" and word3 == "you":
        print(">>>Yes!!! Yes!!! I love you too.")
    else:
        print(">>>You better not have told that.")
else:
    print(">>>Thank you. Bye, now")
