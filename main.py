def main():
    
    frankenstein_book = "books/frankenstein.txt"
    frankenstein_contents = get_file_contents(frankenstein_book)
    frankenstein_words = count_words(frankenstein_contents)
    frankenstein_letters = count_letters(frankenstein_contents)
    generate_report(frankenstein_book)


def get_file_contents(file):
    with open(file) as f:
        return f.read()

def count_words(file):
    words = file.split()
    num_words = len(words)
    return num_words

def count_letters(file):
    letters_dict = {}
    lowered_file = file.lower()
    for f in lowered_file:
        if f in letters_dict:
            letters_dict[f] += 1
        else: 
            letters_dict[f] = 1
    return letters_dict

def sort_on(dict):
    return dict["num"]

def sort_letters(dict):
    letters = []
    items = dict.items()
    for item in items:
        letters.append({"letter": item[0], "num": item[1]})
    letters.sort(reverse=True, key=sort_on)
    for letter in letters:
        if letter["letter"].isalpha() == True:
            print(f"The {letter["letter"]} character was found {letter["num"]} times")

def generate_report(file):
    file_contents = get_file_contents(file)
    file_words = count_words(file_contents)
    file_letters = count_letters(file_contents)
    print(f"--- Begin report of {file} ---")
    print(f"{file_words} words found in the document")
    letters_sorted = sort_letters(file_letters)
    print("--- End report ---")
main()