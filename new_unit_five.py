#Guessing game, created by Caleb Beswick on 10/18/21 for unit five project
#This project creates a guessing game that tells you if your guess is higher, lower, or correct on a number between 1-100
import random




def generating_number():
    """

    :return:
    """
    x = random.randint(1, 101)
    return x

def guessing_game(number):
    """

    :param number: The number randomly selected
    """
    player_guess = 0
    tries = 0
    while player_guess != number:
        player_guess = int(input("Please enter your guess "))
        if player_guess >= number:
            print("The number is less than", player_guess)
        elif player_guess <= number:
            print("The number is more than", player_guess)
        tries = tries + 1
    print("You got it right!")
    print("It took you", tries, "tries!")




def main():
    number = generating_number()
    guessing_game(number)

main()