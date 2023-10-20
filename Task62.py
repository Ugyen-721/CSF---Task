user_inputs = []
for i in range(3):
    user_input = int(input(f"Enter number {i + 1}: "))
    user_inputs.append(user_input)

def is_even(numbers):
    return all(number % 2 == 0 for number in numbers)
result = is_even(user_inputs)
print(f"Are all numbers even? {result}")