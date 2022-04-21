import random        
    
def guessgame() :
    print("welcome to guess the word game where you`ll be entering letters to form a word")

    wordbank = ["while", "yatch", "boat"]
    computer = random.choice(wordbank)

    blanks="".join(["_"] * len(computer))
    print('\n')

    print(blanks)
    print("Here is a hint, the word is", len(computer), "letters long") 

    passes = 3

    while passes > 0 :
        passes -= 1
         
        user = input("guess a letter: ")
        for i in range(len(computer)):
            if computer[i] == user:
                correct_letters = i
                blanks = "".join((blanks[:correct_letters],user,blanks[correct_letters+1:]))
                print(blanks)
        print("Try again")
        if blanks == computer:
            print("You win")
            break
        elif passes == 0:
            print("You lost, Game over!")

    
guessgame()        