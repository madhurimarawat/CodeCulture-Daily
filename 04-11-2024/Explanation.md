# Alternating Number Pattern

## Overview

This program generates a descending pattern of alternating numbers (1 and 0) based on a specified number of rows (`r`). The pattern starts with `1` on the first row, and alternates between `1` and `0` on each subsequent row. Each row contains one fewer element than the previous row until reaching a single element in the last row.

## Requirements

1. **Input**: The program prompts the user to enter an integer `r`, representing the number of rows.
2. **Pattern**:
   - **Odd-numbered rows** start with `1`, and **even-numbered rows** start with `0`.
   - The first row has `r` elements, the second row has `r-1` elements, and so on until the last row, which contains just one element.

## Example

If the input `r` is `5`, the output pattern will be:

```
1 1 1 1 1
0 0 0 0
1 1 1
0 0
1
```

### Code Walkthrough

1. **Input and Initialization**:

   - The program starts by asking the user to input the number of rows, which we store in the variable `r`.
   - A newline is printed to cleanly separate the input prompt from the output pattern.

2. **Loop Through Rows**:

   - We use a `for` loop to iterate from `r` down to `1` (inclusive). This allows us to print each row with one fewer element than the last.
   - In each iteration, we:
     - **Check if the row is even or odd**:
       - If the row number `i` is **even**, we print the character `0`, repeated `i` times, separated by spaces.
       - If the row number `i` is **odd**, we print the character `1`, repeated `i` times, separated by spaces.

3. **Output**:
   - The loop prints each row in descending order, forming the alternating number pattern as per the requirements.

## Additional Notes

- This pattern alternates the starting character (`1` for odd rows and `0` for even rows) and reduces the count of elements in each row.
- The loop ensures each row’s content is centered around its even or odd position, which gives it an alternating look.

This program provides a simple yet effective way to practice loops and conditional statements in Python. It's particularly useful for understanding control flow and pattern-based logic.
