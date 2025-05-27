from stats import (count_words, split_words, make_letter_dict, sort_on, sort_dict)

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
    
def text_stringer(relative_path):
    book_text = get_book_text(relative_path)
    return book_text

split_text = text_stringer(sys.argv[1])
text_string = split_words(split_text)
printed_out = count_words(text_string)
letter_dict = make_letter_dict(text_string)
printed_dict = sort_dict(letter_dict)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {printed_out} total words")
print("--------- Character Count -------")

for item in printed_dict:
    print(f"{item['char']}: {item['num']}")

print("============= END ===============")