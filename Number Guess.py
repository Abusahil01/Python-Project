#Number Guessing Game
import random
from lib2to3.fixes.fix_import import traverse_imports

print("############### Welcome User to NumGuess ###############")
x=input("Press \"Enter\" to start the game:")
print("Rules:")
print("--> Guess a number from 1 to 100")
print("--> You will get 7 chance to *WIN*\n!!!!!!!! Let's Go !!!!!!!!")

num=random.randrange(1,101)
chance=10
chnc=10
count=0
tr=1

print("Number has been picked")

while count<chance:
    guess=int(input(f"Guess the number(Try{tr}):"))
    tr+=1
    count=count+1
    chnc=chnc-1
    if guess==num:
        print(f'Congrates! you guess the correct number {num}, You find it in {count} time')
        break
    elif count>=chance and guess!=num:
        print("You have no chance left\n###############  Better Luck Next Time  ###############")
    elif guess>num:
        print(f"You guess high, Try a lower number\n!!!!! Chance left: {chnc} !!!!!")
    elif guess<num:
        print(f"You guess low, Try a higher number\n!!!!! Chance left: {chnc} !!!!!")

print(f"The number is: {num}")
print("############################# GAME OVER ######################################")