def sort_on(dict):
    return dict["count"]

book = "books/frankenstein.txt"

with open(book) as f:
    file_contents = f.read()

    words = file_contents.split()
    lowercase_content = file_contents.lower()
    letter_count = {}
     
    for char in lowercase_content:
        if not char.isalpha():
            continue
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    letter_list = []

    for letter in letter_count:
        letter_list.append({ "letter": letter, "count": letter_count[letter]}) 

    letter_list.sort(reverse=True, key=sort_on)


    print(f"--- Begin report of {book} ---")
    print(f"{len(words)} words found in this document\n")
    
    for letter in letter_list:
        print(f"The '{letter["letter"]}' character was found {letter["count"]} times")

    print("--- End Report ---")
