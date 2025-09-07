# Let code the program for Rock-Paper-Scissor. Lets Go !!

computer = "scissor"
user = input("enter your choice\n")

if computer == user:
    print("TIE")

elif computer == "scissor" and user == "rock":
    print("WIN")

elif computer == "scissor" and user == "paper":
    print("LOST")

elif computer == "rock" and user == "rock":
    print("TIE")

elif computer == "rock" and user == "paper":
    print("WIN")

elif computer == "rock" and user == "scissor":
    print("LOST")

elif computer == "paper" and user == "paper":
    print("TIE")

elif computer == "paper" and user == "rock":
    print("LOST")

elif computer == "paper" and user == "scissor":
    print("WIN")

else:
    print("good bye")   
