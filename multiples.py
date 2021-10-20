def get_sum(number):
    """
    Will return the sum of all the multiples of 3 or 5 of the given number.
    Ex. get_sum(10) returns 23
    :param number: The value up to which we want to find the sum. Not included in the calculation
    :return: The sum of all the multiples of 3 or 5 up to the number.
    """
    num_2 = number
    total = 0
    for x in range(number):
        if num_2 % 3 == 0 or num_2 % 5 == 0:
            num_2 = num_2 - 1
            total = total + num_2
        else:
            num_2 + 0
    print(num_2)
    return num_2


get_sum(1000)


