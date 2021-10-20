def get_input():
    """
    This function ensures that a user correctly enters in a number in the proper range.
    :return: a value between 1 and 10, inclusive
    """
    while True:
        question = int(input("Please enter a number between 1 and 10 >>> "))
        if 1 <= question <= 10:
            break


def main():
    print(get_input())


if __name__ == '__main__':
    main()
