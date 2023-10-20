user_name = input("Enter your name: ")
vowel_count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}

for char in user_name:
    if char.lower() in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)