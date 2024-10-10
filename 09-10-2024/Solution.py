# 😂 Fun Fact: The Caesar Cipher was so "secure" that Julius Caesar probably thought no one could crack it. Spoiler alert: they did! 🔓

print("Caesar Cipher in Python with Dictionary")


# Creating a dictionary to store both uppercase and lowercase letters mapped to numbers.
# Problem: Lowercase and uppercase letters will have the same shift, so output will always be lowercase.
def alph_dict_make():
    # Initializing the dictionary to store alphabet-to-number mappings
    alph_dict = {}

    # Using a loop to assign each alphabet a numeric value
    for i in range(1, 27):
        # Lowercase letters
        alph_lwr = chr(96 + i)
        alph_dict[alph_lwr] = i

        # Uppercase letters
        alph_upr = chr(64 + i)
        alph_dict[alph_upr] = i

    return alph_dict


# Function to perform Caesar Cipher Encryption and Decryption
# Decryption is done by passing a negative shift value
def Caesar_Cipher(text, n):

    # Encrypting using the dictionary by shifting letters
    encryp_text = ""

    # Looping through each character in the text
    for i in text:
        # % 26 ensures wrapping around the alphabet
        char_value = (alph_dict[i] + n) % 26

        # Find the character based on the new shifted value
        val = next(key for key, value in alph_dict.items() if value == char_value)

        # Adding the new character to the encrypted text
        encryp_text += val

    return encryp_text


# Taking user input
message = input("Enter Message: ")
shift_value = int(input("Enter Shift Value: "))

# Creating the alphabet dictionary
alph_dict = alph_dict_make()

# Encrypting the message
encryp_text = Caesar_Cipher(message, shift_value)
print(
    f"Encrypted Text using Caesar Cipher with Shift value {shift_value} is:",
    encryp_text.upper(),
)

# Decrypting the message
print(
    f"Decrypted Text using Caesar Cipher with Shift value {shift_value} is:",
    Caesar_Cipher(encryp_text, -shift_value),
)
