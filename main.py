
#Count the number of words in a text file
#Assuming the text file is in the same directory as this script
#or provide the full path to the file   



def get_book_text(filepath):
    #defines a function called get_book_text that 1 argument filepath(the lovcation of the text file)
    # read the file and return its content as a string
    with open(filepath, "r", encoding="utf-8") as file:
        # opens the file at filepath in read mode with utf-8 encoding(to handle special characters)
        return file.read()
import sys
from stats import get_num_words
from stats import get_character
from stats import sorted_list
#imports the words function from the stats module

def main():
   
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #defines the main function, which coordinates the execution of the program
    #removed to change to sys module
    #path = "books/frankenstein.txt"
    path = sys.argv[1]
    #specifies the path to the text file set to the variable path
    text = get_book_text(path)
    #calls the get_book_text function with the specified path to read the file's content and stores it in the variable text
    word_count = get_num_words(text)
    #calls the get_num_words function with the text content to count the number of words and stores the result in word_count
    char = get_character(text)
    #calls the get_character function with the text content to get character counts and stores the result in char
    sorted_chars = sorted_list(char)

    char = get_character(text)
    print("DEBUG_t_count:", char.get('t', 0))
    sorted_chars = sorted_list(char)
    print("DEBUG_sorted_t:", next(x for x in sorted_chars if x["char"] == "t"))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END =============")

if __name__ == "__main__":
    main()


