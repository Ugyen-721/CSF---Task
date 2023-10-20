user_number = int(input("Enter a number: "))
factorial = 1
if user_number < 0:
    print("Factorial is undefined for negative numbers.")
else:
    for i in range(1, user_number + 1):
        factorial *= i

    print("Factorial:", factorial)