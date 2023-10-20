num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    num1, num2 = num2, num1
total_sum = 0
current_num = num1
while current_num <= num2:
    total_sum += current_num
    current_num += 1
print(f"The sum of number {num1} and {num2} is: {total_sum}")
