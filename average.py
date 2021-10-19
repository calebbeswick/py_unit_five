def main():
    n = int(input("Enter the amount of numbers"))
    sum = 0.0
    for i in range(n):
        x = int(input("Please enter a number"))
        sum = sum + x
    final = sum / n
    print("The average of the numbers is", final)

main()