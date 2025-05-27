def split_words(book_text):
    split_text = book_text.split()
    return split_text
    
    

def count_words(split_words_str):
    word_count = 0
    for word in split_words_str:
        word_count += 1
    return word_count

def make_letter_dict(string_input):
    letter_dict = {}
    for word in string_input:
        for letter in word:
            letter = letter.lower()
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] =1
    return letter_dict

def sort_on(item):
    return item["num"]

def sort_dict(letter_dict):
    entry_list = []
    for entry in letter_dict:
        if entry.isalpha():
            entry_list.append({"char": entry, "num": letter_dict[entry]})
    entry_list.sort(reverse=True, key=sort_on)
    return entry_list