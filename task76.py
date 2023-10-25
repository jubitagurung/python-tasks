def find_longest_word(input_string):
    words = input_string.split()  # Split the string into words
    longest_word = max(words, key=len)  # Find the word with the maximum length
    return longest_word

# Example usage:
input_string = "This is a simple test string with some words"
result = find_longest_word(input_string)
print(result)  # Output: "simple"





