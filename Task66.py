def calculate_average(numbers):
    if not numbers:
        return None 

    total = sum(numbers)
    average = total / len(numbers)
    return average
numbers_list = [3, 8, 1, 5, 12, 7]
average_value = calculate_average(numbers_list)

print(f"The average of the numbers is: {average_value}")


