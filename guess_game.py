import random
a=int(input("enter number:"))
b=int(input("enter number:"))
randomNo=random.randint(a,b)
guesses=0
userguess=None

while(userguess!=randomNo):
    userguess=int(input(f"Enter your guessed number between {a} and {b}:"))
    guesses+=1
    
    if (userguess==randomNo):
        print("Congragulattion! Your guess is right")
    else:
        if (userguess>randomNo):
            print("Your guess is too high; Please enter small number")
        else:
             print("Your guess is small; Please enter high number")

print(f"You guessed the number in {guesses} guesses")
with open ("hiscore.txt","r") as f:
    hiscore=int(f.read())

if (guesses<hiscore):
    print("Wow! You have broken the high score")
    with open ("hiscore.txt","w") as f:
        f.write(str(guesses))

elif(guesses==hiscore):
    print(f"Well good your score is equal to hiscore {hiscore}")