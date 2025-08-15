from stats import get_num_words

def main(path):
    print(f"{get_num_words(path)} words found in the document")

main("./books/frankenstein.txt")
