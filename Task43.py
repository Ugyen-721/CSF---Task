user_name = input("Enter your name: ")
has_vowel = False
vowels = {'a', 'e', 'i', 'o', 'u'}

for char in user_name:
    if char.lower() in vowels:
        has_vowel = True
        break

print(has_vowel)




