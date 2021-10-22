import random

def get_number():
    """

    :return: returns the randomly generated number
    """
    number = random.randint(1,11)
    return number



def user_inputs():
    """

    :return: returns if the user wants to play or not
    """
    play_game = input("Would you like to play a game of Nim? ")
    if play_game == "y":
        return play_game
    elif play_game == "n":
        return play_game

def playing_game(pile0, pile1):
    stones = 0
    player_move = True
    while pile0 != 0 and pile1 != 0:
        pile_number = int(input("Pile 0 or 1? "))
        if pile_number == 0:
            pile_of_stones = pile0
        elif pile_number == 1:
            pile_of_stones = pile1
        while player_move == True:
            print(pile0)
            print(pile1)
            move = int(input("Please enter the amount of stones you would like to remove from the pile "))
            if move == 1 and pile_of_stones >= 1:
                pile_of_stones = pile_of_stones - move
                player_move = False
            elif move == 2 and pile_of_stones >= 2:
                pile_of_stones = pile_of_stones - move
                player_move = False
            elif move == 3 and pile_of_stones >= 3:
                pile_of_stones = pile_of_stones - move
                player_move = False
            print(pile_of_stones)
            player_move = False
        while player_move == False:
            break







def main():
    pile0 = get_number()
    pile1 = get_number()
    print(pile1)
    print(pile0)
    user_inputs()
    playing_game(pile0, pile1)

main()