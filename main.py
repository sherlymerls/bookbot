import sys

from stats import get_word_count, get_letter_count, create_labelled_list, list_sort

def main():
    #print(sys.argv[0])
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    location = sys.argv[1]
    text = get_book_text(location)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    labelled_list = create_labelled_list(letter_count)
    labelled_list.sort(reverse=True, key=list_sort)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in labelled_list:
        if item["letter"].isalpha() == True:
            print(f"{item["letter"]}: {item["count"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()