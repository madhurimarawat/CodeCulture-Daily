# **Explanation of the Code**

**😂 "Why do programmers love printing patterns? Because they love to _see_ the results! 🤓**

### **Objective:**

The goal of this program is to print a symmetric star (`*`) pattern based on a given number of rows `r`. The pattern starts from a single star and expands symmetrically to a maximum, then descends symmetrically.

### **Code Breakdown:**

1. **Input Handling:**

   - `r = int(input("Enter Number of Rows: "))`: This line takes an integer input from the user, representing the total number of rows for the pattern.
   - `print()`: Adds a blank line for clear spacing before the pattern output.

2. **Loop Structure:**
   - `for i in range(r)`: A `for` loop iterates through each row index from `0` to `r-1`.
3. **Pattern Printing Logic:**

   - **First Half (Ascending):**

     - `if i <= r // 2`: Checks if the current row index `i` is in the first half of the rows.
     - `val = 2 * i + 1`: Calculates the number of stars for the row, following the pattern of incrementing by 2 (i.e., 1, 3, 5, etc.).

   - **Second Half (Descending):**
     - `else`: For rows beyond the midpoint.
     - `val = 2 * (r - i) - 1`: Calculates the number of stars by decrementing the count symmetrically (i.e., 5, 3, 1, etc.).

4. **Printing the Pattern:**
   - `print("* " * val)`: Prints the calculated number of stars, each followed by a space for proper formatting.

### **Example Run:**

#### **Input:**

```plaintext
Enter Number of Rows: 5
```

#### **Output:**

```plaintext
*
* * *
* * * * *
* * *
*
```

### **Explanation of the Output:**

- The first row starts with 1 star.
- The second row prints 3 stars.
- The third row prints 5 stars (the midpoint and widest row).
- The fourth row reverts to 3 stars.
- The fifth row ends with 1 star.

This forms a symmetric pyramid pattern that expands to the midpoint and then reduces symmetrically.

### **Edge Cases:**

- For `r = 1`, only a single `*` will be printed.
- For large values of `r`, the pattern still maintains symmetry as per the logic.
