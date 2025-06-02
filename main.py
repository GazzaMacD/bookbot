from stats import get_num_words, get_char_count


def get_book_text(file_path):
    """Take file path and return contents of file as string"""
    try:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        return f"ERROR: the file at {file_path} was not found"


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    num_chars = get_char_count(text)
    print(f"{num_words} words found in the document")
    print(num_chars)


if __name__ == "__main__":
    main()
