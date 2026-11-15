import random

def get_choices():
    player_choice = input("Enter your choice: ").lower()
    options = ['scissor','rock','paper']
    computer_choice = random.choice(options)
    chosed = {"player" : player_choice , "computer" : computer_choice}
    return chosed

def check_win(player, computer):
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissor":
            print("You won!")
        else :
            print("You lost!")
    elif player == "scissor":
        if computer =="rock":
            print("You lost!")
        else:
            print("You won!")
    elif player == "paper":
        if computer == "rock":
            print("You won!")
        else :
            print("You lost!")
    else :
        print("Enter correct choice")


choice = get_choices()
check_win(choice["player"] , choice["computer"])

