def fibonacci(x):
    """
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
    a = 0
    b = 1
    c = 0
    final = ""

    for i in range(x):
       a = b
       b = c
       c = a + b
       final += str(c) + " "
    return final


