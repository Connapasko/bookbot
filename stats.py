def count_words_in_book(book):
    words = book.split()
    length = len(words)
    return print(f"Found {length} total words")

def count_each_char(booktext):
    char_count = {}
    for char in booktext:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count
