def find_longest_word(input_string):
    words = input_string.split()  
    longest_word = max(words, key=len)
    return longest_word

input_str = "My name is Ugyen Dendup"
longest_word_result = find_longest_word(input_str)

print(f"The longest word is: {longest_word_result}")