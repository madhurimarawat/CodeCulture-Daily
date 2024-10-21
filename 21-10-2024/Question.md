### **Question: Half Pyramid Pattern in C++**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Programming Languages (C++)

**Input:**

- The user is prompted to enter an integer `n` representing the number of rows for the half pyramid.

**Output:**

- The program prints a half-pyramid of stars (`*`) with `n` rows, where the first row contains 1 star, the second row contains 2 stars, and so on.

### **Description:**

In this task, you are required to create a simple half-pyramid pattern using nested loops in C++. The number of rows `n` is taken as input from the user. The pattern grows by one star (`*`) in each subsequent row.

### **Steps:**

1. **Take Input:**

   - The user is asked to input the number of rows `n` for the pyramid.

2. **Loop Structure:**
   - Use two nested `for` loops:
     - The outer loop controls the rows (from 1 to `n`).
     - The inner loop controls the number of stars printed in each row.
3. **Print the Stars:**
   - For each row, print the corresponding number of stars, separated by spaces. At the end of each row, print a newline (`\n`) to move to the next row.

### **Example:**

For `n = 4`, the output will be:

```
*
* *
* * *
* * * *
```
