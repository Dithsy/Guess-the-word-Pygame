import random

print("welcome to guess the word game where you`ll be entering letters to form a word")

wordbank = ["while", "yatch", "boat", "birds"]
computer = random.choice(wordbank)

correct_letters=["-"]*len(computer)
blanks= "".join(correct_letters)
print('\n')

print(blanks)
print("Here is a hint, the word is", len(computer), "letters long")
print("\n") 

passes = 8
while passes > 0:
    passes -= 1
    user = input("guess a letter: ")
    if user in computer:
        for index in range(len(computer)):
            if computer[index] == user:
                correct_letters[index] = user
                blanks= "".join(correct_letters)
        print(blanks)
        print("Your guess was correct!")
        passes += 1

    else:
        print("Your guess was incorrect!")
        print("You have", passes, "passes left")
    
    if blanks == computer:
        print("You win")
        break
    elif passes == 0:
        print("You lost, Game over!")            
