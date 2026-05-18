word_to_find = input("Enter the word to search: ")

count = 0

try:
    
    f = open("sample.txt", "r")

    
    content = f.read()

    
    words = content.split()

    
    for word in words:
        if word.lower() == word_to_find.lower():
            count += 1

    
    f.close()

    print(f"The word '{word_to_find}' occurred {count} times in the file.")

except FileNotFoundError:
    print("File not found.")
