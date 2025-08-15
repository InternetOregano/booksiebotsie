from stats import count_words, count_chars, print_report

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return str(book)

def main():
    path = "./books/frankenstein.txt"
    book_content = get_book_text(path)
    words = count_words(book_content)
    counts_dict = count_chars(book_content)


    print(count_words(book_content))
    print(count_chars(book_content))
    print(print_report(counts_dict))

if __name__== "__main__":
    main()
