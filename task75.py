def reverse_words(input_string):
    words = input_string.split()  # Split the string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words back into a string

# Example usage:
input_string = "Hello, world!"
result = reverse_words(input_string)
print(result)  # Output: "olleH, dlrow!"
