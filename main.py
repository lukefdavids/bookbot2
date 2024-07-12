def main():
    book_path = "books/frankenstein.txt"
    text = read_file(book_path) 
    total_word_count = count_words(text)
    total_character_count = count_characters(text)
    sort_dict = sort_character_dict(total_character_count)
    
    print(f"---Begin report of {book_path}---")
    print()
    print(f"{total_word_count} words found in the document")
    print()
    
    for dict in sort_dict:
        print(f"The letter {dict["char"]} was found {dict["num"]} times")
    
    print()
    print("---End report---")

def read_file(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict

def sort_character_dict(char_dict):
    # This function filters out non alphabetical characters, creates a list of dictionaries and sorts the list 
    
    list_of_dicts = []
    filtered_char_dict = {}

    for key, value in char_dict.items():
        if key.isalpha():
            filtered_char_dict[key] = value
    
    for key, value in filtered_char_dict.items():
        list_of_dicts.append({"char": key, "num": value})
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    return list_of_dicts
    
        
main()