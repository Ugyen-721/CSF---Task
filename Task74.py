def reverse_words(input_string):
    words = input_string.split() 
    reversed_words = [word[::-1] for word in words]
    result_string = ' '.join(reversed_words)
    return result_string

input_str = "Hello, world!"
reversed_result = reverse_words(input_str)

print(f"Original string: {input_str}")
print(f"String with reversed words: {reversed_result}")