letter=input('enter a letter')
if(len(letter)==1):
    if(letter.isalpha()):
        if letter.lower() in "aeoiu":
            print("letter is vowel")
        else:
            print("letter is not vowel")
    else:
        print("you enter number so please enter a letter ")
else:
    print("please enter one letter")





    

