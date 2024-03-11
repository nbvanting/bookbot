

def return_content(filepath) -> str:
    with open(filepath) as f:
        content = f.read()  
    return content


def count_words(filepath) -> int:
    content = return_content(filepath)
    word_count = len(content.split())
    return word_count

def count_letters(filepath) -> dict:
    content = return_content(filepath).lower()
    letter_dict = {}
    for letter in content:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def convert_dict(dict) -> list:
    list = []
    for key, value in dict.items():
        list.append({"character": key, "num": value})
    return list

def sort_on(dict) -> dict:
    return dict["num"]

def summarize_book(filepath) -> None:
    print(f"--- Begin report of {filepath} ---")
    print(f"{count_words(filepath)} words found in the document\n")
    letters = convert_dict(count_letters(filepath))
    letters.sort(reverse=True, key=sort_on)
    for l in letters:
        if l["character"].isalpha():
            print(f"The '{l["character"]}' character was found {l["num"]} times")
    print("--- End report ---")
    

def main():
    filepath = "books/frankenstein.txt"
    # words = count_words(filepath)
    # print(words)
    # letters = count_letters(filepath)
    # print(letters)
    summarize_book(filepath)

main()