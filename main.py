def main():
    book_path = "books/frankenstein.txt"
    text = read_file(book_path) 
    total_word_count = count_words(text)
    print(total_word_count)

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

main()