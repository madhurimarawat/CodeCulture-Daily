## Explanation

**What’s a programmer’s favorite Diwali ritual?**

```python
try:
    lighting diyas!
except:
    getting burnt! 🔥
```

**So be safe, do coding, and light the emoji diyas—they are safe!** 🌟

### Overview

The Diya Harmony Pattern Printer is a simple yet charming program that prints a symmetrical pattern of colored diyas using emojis. The user specifies the number of rows, and the program generates a visually appealing arrangement of emojis representing different colored diyas.

### Code Breakdown

```python
# Number of Rows
try:
    r = int(input("Enter Number of Rows: "))
```

1. **User Input:**
   - The program begins by prompting the user to enter the desired number of rows. This value is stored in the variable `r`.
   - The `try` block is used to catch potential errors when converting the user input to an integer. If the user enters something that cannot be converted (like a string or a special character), it raises a `ValueError`.

```python
# List of diyas
diyas = ["🔴", "🟡", "⚪", "🟢", "🔵"]
```

2. **Emoji List:**
   - We create a list called `diyas` that contains five different colored diya emojis: Red, Yellow, White, Green, and Blue.

```python
print()
```

3. **New Line:**
   - An empty `print()` statement is used to create a blank line for better output formatting.

```python
# Loop to Print Pattern
for i in range(0, r):
```

4. **Outer Loop:**
   - This loop iterates from `0` to `r - 1`. The variable `i` represents the current row number.

```python
    for j in range(0, r):
```

5. **Inner Loop:**
   - Nested within the outer loop, this loop also iterates from `0` to `r - 1`. The variable `j` represents the position of the emoji within the current row.

```python
        print(diyas[(i + j) % len(diyas)], end=" ")
```

6. **Printing Emojis:**
   - In this line, we print the emoji for the current position in the row.
   - The expression `(i + j) % len(diyas)` calculates the index of the emoji to be printed:
     - `i + j` calculates the current index by summing the row and position values.
     - The modulus operator `%` is used to wrap around the index, ensuring that it cycles through the available emojis in the list.
   - The `end=" "` argument in the `print()` function ensures that all emojis in the row are printed on the same line, separated by spaces.

```python
    print()
```

7. **New Line for Next Row:**
   - After completing the inner loop for a particular row, we call `print()` again (without arguments) to move to the next line for the subsequent row's output.

### Handling Invalid Input

```python
except ValueError:
    print("Please enter a valid integer for the number of rows.")
```

- **Error Handling:**
  - The `except` block catches any `ValueError` that arises when the user inputs a non-integer value.
  - When an invalid input is detected, the program prints a friendly message: "Please enter a valid integer for the number of rows." This guides the user to provide correct input without crashing the program.

### Pattern Repetition

- If the user enters a value for \( r \) greater than 5, the program will repeat the same pattern using the modulus operation. For example, if \( r = 7 \), the program generates the following output:

#### Example for \( r = 7 \)

- **Input:**
  ```
  Enter Number of Rows: 7
  ```
- **Output:**
  ```
  🔴 🟡 ⚪ 🟢 🔵 🔴 🟡
  🟡 ⚪ 🟢 🔵 🔴 🟡 ⚪
  ⚪ 🟢 🔵 🔴 🟡 ⚪ 🟢
  🟢 🔵 🔴 🟡 ⚪ 🟢 🔵
  🔵 🔴 🟡 ⚪ 🟢 🔵 🔴
  🔴 🟡 ⚪ 🟢 🔵 🔴 🟡
  🟡 ⚪ 🟢 🔵 🔴 🟡 ⚪
  ```

### Explanation of the Pattern Repetition

- In this example, for \( r = 7 \):
  - The first row starts with the first emoji (🔴) and continues through all five emojis.
  - When it reaches the end of the list, it uses the modulus operation to cycle back to the start.
  - Thus, the sixth and seventh rows repeat the pattern from the beginning, effectively showing that the program reuses the emoji sequence to fill additional rows beyond the fifth. 💡

### Conclusion

This simple program effectively demonstrates the use of loops and modular arithmetic to create a charming pattern with colored diyas represented by emojis. The clear structure and use of Python's list allow for easy modifications and adaptations for other patterns or designs.
