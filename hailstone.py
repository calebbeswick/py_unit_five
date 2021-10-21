def sequence(number):
    """
    If the number n is odd - 3*n + 1
    If the number n is even n / 2
    :param number: The starting number for the Hailstone sequence
    :return: The number of steps taken to reach 1
    """
    length_of_cycle = 1

    while number != 1:

        if number % 2 == 0:
            number = number / 2
            length_of_cycle = length_of_cycle + 1
        else:
            number = (number * 3) + 1
            length_of_cycle = length_of_cycle + 1
    print(length_of_cycle)
    return length_of_cycle





