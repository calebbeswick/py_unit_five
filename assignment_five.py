#Caleb Beswick 10/26 creates a game on Nims
# ***Not working yet***
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
    """

    :param pile0: The first pile of stones
    :param pile1: The second pile of stones
    :return:
    """
    player_move = True
    while pile0 != 0 and pile1 != 0:
        pile_number = int(input("Pile 0 or 1? "))
        if pile_number == 0:
            pile_of_stones = pile0
            not_pile_of_stones = pile1
        elif pile_number == 1:
            pile_of_stones = pile1
            not_pile_of_stones = pile0
        while player_move == True:
            print(pile0)
            print(pile1)
            move = int(input("Please enter the amount of stones you would like to remove from the pile "))
            if move == 1 and pile_of_stones >= 1:
                pile_of_stones = pile_of_stones - move
            elif move == 2 and pile_of_stones >= 2:
                pile_of_stones = pile_of_stones - move
            elif move == 3 and pile_of_stones >= 3:
                pile_of_stones = pile_of_stones - move
            if pile0 == 0 or pile1 == 0:
                print("You won!")
                break
            player_move = False
        while not player_move:
            comp_move = random.randint(1, 3)
            pile = random.randint(0, 1)
            if pile_of_stones == pile0 -- move:
            if pile == 0:
                if pile0 >= comp_move:
                    pile0 = pile0 - comp_move
                    print("The computer moved", comp_move, "from pile 0")
                    player_move = True
            elif pile == 1:
                if pile1 >= comp_move:
                    pile1 = pile1 - comp_move
                    player_move = True
            if pile0 == 0 and pile1 == 0:
                print("The computer won!")








def main():
    pile0 = get_number()
    pile1 = get_number()
    print(pile0)
    print(pile1)
    user_inputs()
    playing_game(pile0, pile1)

main()