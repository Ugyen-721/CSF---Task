user_name = input("Enter your name: ")
vowel_count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
index = 0

while index < len(user_name):
    if user_name[index].lower() in vowels:
        vowel_count += 1
    index += 1

print("Number of vowels:", vowel_count)