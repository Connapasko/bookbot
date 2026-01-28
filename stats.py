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


def sort_on_num(items):
    return items["num"]

def sort_char_counts(char_counts):
    char_list = []
    for char in char_counts:
        if char.isalpha():
            char_list.append({
                "char":char,
                "num": char_counts[char]
            
            })
    char_list.sort(reverse=True, key=sort_on_num )
    return (char_list)
