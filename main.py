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

def generate_report(full_path):
    words = get_word_list(full_path)
    letters = get_letter_count(words)
    letters = dict(sorted(letters.items(), reverse=True, key=lambda item: item[1]))
    for letter in letters:
        print(f"Character '{letter}'  was found {letters[letter]} times")

def main():
    generate_report("./BOOKS/frankenstein.txt")

main()
