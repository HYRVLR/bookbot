from stats import count_words, get_chars_dict, chars_dict_to_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book filepath from command line arguments
    filepath = sys.argv[1]

    try:
        book_text = get_book_text(filepath)
        word_count = count_words(book_text)
        chars_dict = get_chars_dict(book_text)
        sorted_chars_list = chars_dict_to_sorted_list(chars_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        # Print each character and its count
        for char_info in sorted_chars_list:
            char = char_info["char"]
            count = char_info["num"]
            # Skip non-alphabetic characters
            if char.isalpha() or char in ['æ', 'â', 'ê', 'ë', 'ô']:
                print(f"{char}: {count}")

        print("============= END ===============")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()