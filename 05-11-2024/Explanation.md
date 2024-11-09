# Pattern Printing Explanation

**Printing letters like there's no tomorrow! 🅰️➡️🅿️**

## Overview

This Python script prints an alphabetical pattern based on user input. The pattern starts with 'A' and continues up to as many letters as specified by the user.

### Example Output

For `r = 5`, the output will be:

```
A
BB
CCC
DDDD
EEEEE
```

### Breakdown of Code

1. **User Input (`r`)**: The script first asks the user to input the number of rows (`r`), which determines how many lines the pattern will have.

   ```python
   r = int(input("Enter Number of Rows: "))
   ```

2. **Newline for Formatting**: A blank `print()` statement ensures the output starts on a new line after the input prompt.

   ```python
   print()
   ```

3. **Setting Up Characters**:

   - `start` is initialized to the ASCII value of 'A' using `ord('A')`, which returns 65.
   - `end` is calculated by adding `r` to `start`, defining the ASCII range for the pattern.

   ```python
   start = ord('A')
   end = start + r
   ```

4. **Loop for Pattern Generation**:
   - The `for` loop iterates from `start` to `end`.
   - `chr(i)` converts the current ASCII value to its corresponding character.
   - The multiplication (`*`) ensures that each character is printed the correct number of times, calculated by `(i + 1 - 65)`. This logic makes 'A' print once, 'B' twice, and so on.
   ```python
   for i in range(start, end):
       print(chr(i) * (i + 1 - 65))
   ```

### Explanation of Key Parts

- **`ord()` Function**: Converts a character to its ASCII value.
- **`chr()` Function**: Converts an ASCII value back to its character.
- **`print()` Statement**: Outputs characters in the desired repeated format, creating the vertical pattern.

### Customization

- Change the starting character by modifying `start`.
- Adjust the pattern by changing how the repetition is calculated in the `print()` statement.
