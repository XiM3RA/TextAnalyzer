import re

def get_word_list(full_path) -> list:
    with open(full_path) as f:
        file_contents = f.read()

    words = [re.sub(r'[^\w\s]','',x) for x in file_contents.split()]
    return words

def get_letter_count(word_list) -> dict:
    #Initialize dictionary of lower case letters
    letters = {chr(i+96):0 for i in range(1,27)}

    for word in word_list:
        for letter in word:
            if (letter.isalpha()):
                temp = letter.lower()
                letters[temp] += 1
    return letters

def main():
    a = get_word_list("./BOOKS/frankenstein.txt")
    b = get_letter_count(a)
    print(b)

main()
