from stats import get_num_words
from stats import how_many_char
def main(path):
    print(f"{get_num_words(path)} words found in the document")
    print(how_many_char(path))

main("./books/frankenstein.txt")
