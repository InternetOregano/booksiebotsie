import sys
from stats import count_words, count_chars, sort_counts

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return str(book)

def main():
    path = sys.argv[1]
    book_content = get_book_text(path)
    words = count_words(book_content)
    counts_dict = count_chars(book_content)
    sorted_dict = sort_counts(counts_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    #loop through list of dictionaries
    for entry in sorted_dict:
        if entry["char"].isalpha() is True:
            print(f"{entry["char"]}: {entry["num"]}")

if __name__== "__main__" and len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
