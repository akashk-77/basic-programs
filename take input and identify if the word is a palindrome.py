word = input("Enter a word: ")

reverse = ""
i = len(word) - 1

while i >= 0:
    reverse = reverse + word[i]
    i = i - 1

if word == reverse:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
