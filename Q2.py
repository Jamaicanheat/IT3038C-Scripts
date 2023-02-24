# Define the list of words to search for
search_words = ["apple", "banana", "orange"]

# Open the text file and read its contents
with open("input.txt", "r") as f:
    text = f.read()

# Split the text into individual words
words = text.split()

# Iterate over the words and output the ones that match the search words
for word in words:
    if word.lower() in search_words:
        print(word)
