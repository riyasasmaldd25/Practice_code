# Let code the program for Rock-Paper-Scissor. Lets Go !!
import random

computer = random.choice(['rock','paper','scissors'])
user = input("enter your choice\n").strip().lower()

print(f"computer choice is : {computer}")

if computer == user:
    print("TIE")
    print("computer chose" + str(computer))

elif computer == "scissors" and user == "rock":
    print("WIN")
    

elif computer == "scissors" and user == "paper":
    print("LOST")
    

elif computer == "rock" and user == "rock":
    print("TIE")
    

elif computer == "rock" and user == "paper":
    print("WIN")
    
elif computer == "rock" and user == "scissors":
    print("LOST")
    

elif computer == "paper" and user == "paper":
    print("TIE")
    

elif computer == "paper" and user == "rock":
    print("LOST")
    

elif computer == "paper" and user == "scissors":
    print("WIN")
    

else:
    print("good bye")   
