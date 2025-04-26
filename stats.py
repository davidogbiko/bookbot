def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def word_count(book):
    words = len(book.split(None))
    return words


def char_count(book):
    chars = {}
    for char in book.lower():
        try:
            chars[char] += 1
        except KeyError:
            chars[char] = 1
    return chars


def sorted_char_count(chars):
    sorted_list = []
    for key, value in chars.items():
        if not key.isalpha():
            continue
        sorted_list.append({"char": key, "num": value})
    sorted_list = sorted(sorted_list, key=lambda item: item["num"], reverse=True)
    return sorted_list
