
from stats import count_words_in_book, count_each_char, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents



def main():
    word_input = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count_words_in_book(word_input)
    print("--------- Character Count -------")
    char_counts = count_each_char(word_input)
    sorted_chars = sort_char_counts(char_counts)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()