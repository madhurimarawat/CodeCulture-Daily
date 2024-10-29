# Taking Input
N = int(input("Enter Number of Words: "))

# List to Store Words
word_list = []

# Loop to collect words
for i in range(N):
    word = input(f"Enter Word {i+1}: ")
    word_list.append(word)


def word_row_type(w):
    # Convert the word to uppercase to match keyboard row format
    w = w.upper()

    # Rows on American keyboard
    rows = ["QWERTPOIUY", "ASDFLKJGH", "ZXCVMNB"]

    # Check if all characters of the word can be typed using only one row
    if any(all(char in row for char in w) for row in rows):
        return 1  # Return 1 if the word can be typed on a single row


# List of words that can be typed from a single row
word_typable = [w for w in word_list if (word_row_type(w) == 1)]

print("Words that can be typed from One Row Of American Keyboard are:")
print(word_typable)
