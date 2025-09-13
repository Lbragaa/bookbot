

def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def num_each_char(book_text):

    char_dict = dict()

    for letter in book_text:
        l = letter.lower()
        if l not in char_dict:
            char_dict[l] = 1
        else:
            char_dict[l] += 1
    
    return char_dict

def dict_list_sort(char_dict):

    sort_list = []
    for key, value in char_dict.items():
        current_char_dict = dict()
        current_char_dict["char"] = key
        current_char_dict["num"] = value
        sort_list.append(current_char_dict)

    sort_list.sort(reverse=True, key = sort_on)
    return sort_list

def sort_on(items):
    #this is used so that they are ordered by the value present in "num"
    return items["num"]

# def num_each_char(book_text):
#     counts = {}
#     for ch in book_text.lower():
#         counts[ch] = counts.get(ch, 0) + 1
#     return counts


# from collections import Counter

# def num_each_char(book_text):
#     return Counter(book_text.lower())

