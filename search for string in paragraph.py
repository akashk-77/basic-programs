paragraph = input("Enter a paragraph:\n")
word = input("Enter the word to search: ")


paragraph_lower = paragraph.lower()
word_lower = word.lower()   #converting to lowercase to search


words = paragraph_lower.split()   #splits paragraph into words


if word_lower in words:

    
    position = words.index(word_lower)

    print(f'"{word}" found in the paragraph.')
    print("Position:", position)

else:
    print(f'"{word}" not found in the paragraph.')
