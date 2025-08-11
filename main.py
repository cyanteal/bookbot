from stats import word_count, character_count, sorting, sort_on
import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = word_count(text)
    characters = character_count(text)
    sorted_count_list = sorting(characters)
    sorted_count_list.sort(reverse=True, key=sort_on)
    #Print Message
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for char in sorted_count_list:
        if str.isalpha(char["char"]):
            print(f"{char["char"]}: {char["num"]}")
    

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()




main()