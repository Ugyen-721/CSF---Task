def multiply_lists(list1, list2):
    result = [a * b for a, b in zip(list1, list2)]
    return result

List1 = [1, 2, 3]
List2 = [4, 5, 6]
result_multiply = multiply_lists(List1, List2)

print(f"The product of the corresponding elements is: {result_multiply}")