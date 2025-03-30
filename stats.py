def get_word_count(text):
    full_text = text.split()
    counter = 0
    for word in full_text:
        counter += 1
    return counter

def get_letter_count(text):
    new_next = text.lower()
    letter_count = {}
    for letter in new_next:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def create_labelled_list(orig_dict):
    count_list = []
    for item in orig_dict:
        new_dict = {}
        new_dict["letter"] = item
        new_dict["count"] = orig_dict[item]
        count_list.append(new_dict)
    return count_list

def list_sort(sort_item):
    return sort_item["count"]