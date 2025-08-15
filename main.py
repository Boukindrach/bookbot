from stats import get_num_words, how_many_char, nice_report

def main(path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path)} total words")
    print("--------- Character Count -------")
    print(nice_report(path))
    print("============= END ===============")

main("./books/frankenstein.txt")
