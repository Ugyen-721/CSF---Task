#task 22
number1 = "1"
number2 = 1
type_of_number1 = type(number1)
type_of_number2 = type(number2)
result = number1 == str(number2)
print("Type of number1:", type_of_number1)
print("Type of number2:", type_of_number2)
print(result)
#The reason why the output is False is because number1 is a string ("1") and number2 is an integer (1).
