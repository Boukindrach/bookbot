from stats import text_to_number
from stats import letters_num
from stats import analyze_letters

def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
    return file_content


def main():
    text = get_book_text("books/frankenstein.txt")
    # print(text_to_number(text))
    # print(letters_num(text))
    analyze_letters(text)

main()
