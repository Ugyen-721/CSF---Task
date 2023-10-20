user_input = int(input("Enter a number: "))

def is_even(number):
    return number % 2 == 0
result = is_even(user_input)
print(f" Is {user_input} even? {result}")