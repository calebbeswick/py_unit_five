def sequence(number):
    """
    If the number n is odd - 3*n + 1
    If the number n is even n / 2
    :param number: The starting number for the Hailstone sequence
    :return: The number of steps taken to reach 1
    """
    total = 1
    while number != 1:
        print(total)
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
        total = total + 1

        return total



sequence(13)