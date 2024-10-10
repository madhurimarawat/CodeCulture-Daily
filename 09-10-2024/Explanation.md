# Implementing Caesar Cipher in Python

## Overview

The Caesar Cipher is a basic encryption method where letters in a message are shifted by a certain number of positions in the alphabet. For example, with a shift of 3, A becomes D, B becomes E, and so on.

In this Python implementation, a dictionary is used to store both uppercase and lowercase letters, and each letter is assigned a numeric value. This dictionary allows us to shift characters efficiently for encryption and decryption.

## Functions

- `alph_dict_make()`: This function creates a dictionary mapping each letter of the alphabet to a corresponding numeric value (both uppercase and lowercase).
- `Caesar_Cipher(text, n)`: This function encrypts or decrypts the text based on the shift value `n`. Encryption is done by adding the shift value to the letter, and decryption is achieved by subtracting the shift value.

## Key Points

- Handles both uppercase and lowercase letters.
- Supports custom shift values.
- Uses modulo 26 to wrap around the alphabet.

## Input and Output

The user provides a message and a shift value. The program outputs both the encrypted and decrypted messages.

### Example:

```

Input:
Message: Hello
Shift: 3

Output:
Encrypted Text: KHOOR
Decrypted Text: HELLO

```

## Why This Approach?

This approach is efficient because we use a dictionary for fast lookups and mappings between letters and their corresponding values. Additionally, we handle both encryption and decryption using a single function, simply by adjusting the shift value for decryption.
