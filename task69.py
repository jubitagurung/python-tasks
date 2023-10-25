def count_chars(input_string, characters):
    count = 0
    
    for chars in input_string:
        if chars == characters:
            count += 1
        return count