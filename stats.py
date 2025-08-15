def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def get_num_words(filepath):
    i = 0
    text = get_book_text(filepath)
    for word in text.split():
        i += 1
    return i

def how_many_char(filepath):
    num_char = {}
    text = get_book_text(filepath)
    text = text.lower()
    for char in text:
        if char.isalpha():
            num_char[char] = num_char.get(char, 0) + 1
    return num_char

def nice_report(filepath):
    char_counts = how_many_char(filepath)
    items_list = list(char_counts.items())
    items_list.sort(key=lambda x: x[1], reverse=True)
    nice_list = []
    for i in items_list:
        s = ""
        for j in range(len(i)):
            s += str(i[j])
            if j == 0:
                s += ": "
        nice_list.append(s)
    return " \n".join(nice_list)
