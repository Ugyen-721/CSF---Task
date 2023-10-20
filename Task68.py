def capitalize_words(input_string):
    words = input_string.split()  
    capitalized_words = [word.capitalize() for word in words]
    result_string = ' '.join(capitalized_words)
    return result_string

input_str = "hello world"
capitalized_result = capitalize_words(input_str)

print(f"Original string: {input_str}")
print(f"Capitalized string: {capitalized_result}")