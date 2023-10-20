def find_max(numbers):
    if not numbers:
        return None

    max_value = numbers[0] 

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value

numbers_list = [3, 8, 1, 5, 12, 7]
maximum_value = find_max(numbers_list)

print(f"The maximum value in the list is: {maximum_value}")