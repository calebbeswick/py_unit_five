import random

def get_number():
    """

    :return:
    """
    number = random.randint(1,11)
    return number



def user_inputs():
    play_game = input("Would you like to play a game of Nim? ")
    if play_game == "y":
        return play_game
    elif play_game == "n":
        return play_game


def playing_game(pile0, pile1):
    pile_number = input("Pile 1 or 0? ")
    pile_total = 0
    if pile_number == 0:
        pile_total = pile0
    elif pile_number == 1:
        pile_total = pile1
    while pile_total != 100:
        print(pile0)
        print(pile1)
        move = input("Please enter the amount of stones you would like to remove from the pile")
        if move == 1 and pile_total >= 1:
            pile_total = pile_total - move
        elif move == 2 and pile_total >= 2:
            pile_total = pile_total - move
        elif move == 3 and pile_total >= 3:
            pile_total = pile_total - move
        computer_move()

def computer_move():
    comp_move = random.randint(1, 4)
    return comp_move


def main():
    pile0 = get_number()
    pile1 = get_number()
    print(pile1)
    print(pile0)
    user_inputs()
    playing_game(pile0, pile1)

main()