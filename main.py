def main():
    path = "./books/frankenstein.txt"


    def get_book_text(filepath):
        with open(filepath) as f:
            book = f.read()
        return book

    book_content = get_book_text(path)

    def count_words(text):
        num_words = 0
        words = text.split()
        for word in words:
            num_words += 1
        return f"{num_words} words found in the document"

    print(count_words(book_content))

main()