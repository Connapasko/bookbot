
from stats import count_words_in_book, count_each_char

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents



def main():
    word_input = get_book_text("books/frankenstein.txt")
    count_words_in_book(word_input)
    print(count_each_char(word_input))

main()