def count_chars(input_string, char):
    count = 0
    for c in input_string:
        if c == char:
            count += 1
    return count

input_str = "hello world"
character_to_count = 'l'
result_count = count_chars(input_str, character_to_count)

print(f"The character '{character_to_count}' appears {result_count} times in the string.")