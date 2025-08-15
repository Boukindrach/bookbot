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
