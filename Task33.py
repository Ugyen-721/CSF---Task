grade = input("Enter your grade: ")

grade = int(grade)
if grade >= 90:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
else:
    print("F")