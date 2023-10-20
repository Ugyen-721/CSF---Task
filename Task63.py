def is_even(user_inputs):
    for number in user_inputs:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

user_inputs = []
for i in range(3):
    user_input = int(input(f"Enter number {i + 1}: "))
    user_inputs.append(user_input)
is_even(user_inputs)