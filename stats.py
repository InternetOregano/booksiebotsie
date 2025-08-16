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
            # get() method will retrieve only the value once the key is set and increment it by 1
            char_count[i] = char_count.get(i, 0) + 1

    return char_count

def sort_counts(counts):
    sorted_counts = []
    for key in counts:
        temp_dict = {}
        temp_dict = {"char": key, "num": counts[key]}
        sorted_counts.append(temp_dict)
    
    def sort_by_count(key):
        return key["num"]

    sorted_counts.sort(reverse=True, key=sort_by_count)

    return sorted_counts
