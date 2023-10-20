user_name = input("Enter your name: ")
has_vowel = False
vowels = {'a', 'e', 'i', 'o', 'u'}
index = 0
while index < len(user_name) and not has_vowel:
    if user_name[index].lower() in vowels:
        has_vowel = True
    index += 1

print(has_vowel)