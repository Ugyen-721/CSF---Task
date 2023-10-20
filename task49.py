import random
secret_number = random.randint(1, 100)

for attempt in range(1, float('inf')):
    user_guess = int(input("Guess the secret number (between 1 and 100 inclusive): "))
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number: {secret_number}")