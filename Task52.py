number = int(input("Enter a number: "))
counter = 1

while counter <= 20:
    result = number * counter
    print(f"{number} * {counter} = {result}")
    counter += 1