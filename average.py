

def calculating_average():
    user_input = ""
    total = 0
    times = 0
    while user_input != "q":
        user_input = input("Please enter a number >>> ")

        if user_input != "q":
            total = total + int(user_input)
            times = times + 1
        elif user_input == "q":
            answer = total / times
            print(answer)
            return answer
            break





calculating_average()