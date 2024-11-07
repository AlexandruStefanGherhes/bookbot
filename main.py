def main():
    book_directory = "books/frankestein.txt"
    text = get_book_text(book_directory)
    letter_tally = repeatingLetters(text)
    total = 0
    for each in letter_tally:
        total += letter_tally[each]
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total} words were found in the document")
    for item in letter_tally:
        print(f"The {item} character was found {letter_tally[item]} times" )

def get_book_text(path):
    with open(path, "r") as book:
        return book.read()

def repeatingLetters(book):
    # splitting the text into words then letters
    words = book.split()
    letters = [char.lower() for word in words for char in word if char.isalpha()]
    # print(letters)
    result = {}
    for letter in letters:
        result[letter] = result.get(letter,0) + 1
    sortedResult = dict(result.items())
    return sortedResult
    
    # print(result)

# def repeatingLetters(book):
#     with open(book,"r") as f:
#         file_contents = f.read()
#         # splitting the text into words then letters
#         words = file_contents.split()
#         letters = [char.lower() for word in words for char in word if char.isalpha()]
#         # print(letters)
#         result = {}
#         for letter in letters:
#             result[letter] = result.get(letter,0) + 1
#         sortedResult = dict(result.items())
#         for item in sortedResult:
#             print(f"{item}:{sortedResult[item]}" )
        # print(result)
    
main()