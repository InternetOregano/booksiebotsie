def count_words(text):
    num_words = 0
    words = text.split()
    for word in words:
        num_words += 1
    return num_words

def count_chars(text):
    # Convert text to lowercase string and initialize dictionary
    lower_text = str(text.lower())
    char_count = {}


    #Loop through all characters in text and set the current character as variable
    for i in lower_text:
        # Check if current character is already in the dictionary
        if i in char_count:
            # Increase the counter in the dictionary if the current_char is present
            char_count[i] += 1
        else:
            # If character is not in dictionary update the key with the value 0 and increment at once
            # get() method will only retrieve the value once the key is set and increment it by 1
            char_count[i] = char_count.get(i, 0) + 1

    return char_count

def print_report(counts):
    sorted_counts = []

    





    # print("============ BOOKBOT ============")
    # print("----------- Word Count ----------")
    # print(f" Found {num_words} total words")
    # print("--------- Character Count -------")
    # print(f"{sorted_counts}")