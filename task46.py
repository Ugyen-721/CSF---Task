user_number = int(input("Enter a number: "))
factorial = 1
if user_number < 0:
    print("Factorial is undefined for negative numbers.")
else:
    while user_number > 0:
        factorial *= user_number
        user_number -= 1

    print("Factorial:", factorial)





