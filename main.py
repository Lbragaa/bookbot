from stats import count_words, num_each_char, dict_list_sort
import sys


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    content = get_book_text(book_path)
    words = count_words(content)
    char_d = num_each_char(content)

    # python
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    
    sorted_dicts = dict_list_sort(char_d)

    for current_dict in sorted_dicts:
        c = current_dict["char"]
        if c.isalpha():
            print(f"{c}: {current_dict['num']}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


if __name__ == "__main__":
    main()

# def main():
#     content = get_book_text("books/frankenstein.txt")
#     words = count_words(content)
#     char_dict = num_each_char(content)
#     print(f"{words} words found in the document")
#     print(dict(sorted(char_dict.items())))