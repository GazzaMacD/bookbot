import sys

from stats import get_num_words, get_char_count, sorted_char_count


def get_book_text(file_path):
    """Take file path and return contents of file as string"""
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Error: Sorry please check the usage note below to avoid errors.")
        print(
            "Usage: Please add the relative path to the target file after the main.py argument"
        )
        print("Example: python3 main.py books/mybook.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    num_chars = get_char_count(text)
    sorted_chars = sorted_char_count(num_chars)
    # Print doc
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
