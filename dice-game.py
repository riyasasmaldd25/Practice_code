import random


def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input('enter name player 1\n')
    player2 = input('enter name player 2\n')

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, ' rolled' , roll1)
    print(player2 , ' rolled' , roll2)

    if(roll1 > roll2):
        print('Player 1 WINS!!')

    elif(roll1 == roll2):
        print('Roll Again')

    else:
        print('Player 2 WINS!!')

main()