def text_to_number(s):
    list_ = s.split()
    return f'{len(list_)} words found in the document'

def letters_num(s):
    list_ = s.split()
    j = 0
    new = {}
    for i in list_:
        for j in range(len(i)):
            if i[j].lower() in new:
                new[i[j].lower()] += 1
            else:
                new[i[j].lower()] = 1
    return new


def analyze_letters(s):
    new = sorted(letters_num(s).items(), key=lambda item: item[1], reverse=True)
    num = len(s.split())
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for k, v in new:
        print(f"{k}: {v}")
    print("============= END ===============")


