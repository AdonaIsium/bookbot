def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_list = get_char_count(text)
    report_output(character_list, num_words, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for char in text:
        l_char = char.lower()
        if l_char.isalpha():
            if l_char in char_dict:
                char_dict[l_char] += 1
            else:
                char_dict[l_char] = 1
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

def report_output(dict, words, path):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in document\n")
    for key, value in dict.items():
        print(f"The '{key}' character was found {value} times")
    print(f"\n--- End report ---")


if __name__ == "__main__":
    main()

