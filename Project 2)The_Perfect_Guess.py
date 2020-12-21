import random
# selecting a random number between 1 to 100 by using random module.
randNumber=random.randint(1,100)
userGuess=None
guess=0
#We will take input from the user until he guesses the correct number.
while userGuess!=randNumber:
    userGuess=int(input("Enter your Guess: "))
    guess+=1
    if userGuess==randNumber:
        print("You guessed it right!")
    elif userGuess>randNumber:
        print("You guessed it wrong! Aim smaller ")
    else:
        print("You guessed it wrong! Aim Larger")
# Printing the number of guesses taken.
print(f"You guessed the number in {guess} guesses")
#Opening or reading the highscore file.
with open("highscore.txt","r") as f:
    highscore=int(f.read())
#Updating the highscore if broken.
if guess<highscore:
    print("You have just broken the highscore! ")
    with open("highscore.txt","w") as f:
        f.write(str(guess))

