def is_sorted(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

sorted_list = [1, 2, 3, 5, 8]
unsorted_list = [4, 2, 7, 1, 9]

print(f"Is the sorted list actually sorted? {is_sorted(sorted_list)}")
print(f"Is the unsorted list sorted? {is_sorted(unsorted_list)}")