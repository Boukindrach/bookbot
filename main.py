from stats import text_to_number
from stats import letters_num
from stats import analyze_letters
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
    return file_content


def main():
    # print(text_to_number(text))
    # print(letters_num(text))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(f"{sys.argv[1]}")
        analyze_letters(text)

main()
