import random

roll = random.randint(1,6)

guess = int(input("take a guess for the dice roll\n"))

if guess == roll:
    print("you are correct  " + str(roll) + "  is the computer guessed")

else:
    print("sorry  " + str(roll) + "  is the computer guessed")