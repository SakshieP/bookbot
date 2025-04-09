import sys
from stats import get_num_words, get_char_count, sort_char_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char_counts = sort_char_counts(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()