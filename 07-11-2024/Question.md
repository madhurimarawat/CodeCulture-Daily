### **Question: Pattern Printing Question**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Patterns and Loops

### **Objective:**

Given an integer input `n`, print the following pattern:

### **Problem Description:**

You need to create a program that prints a pattern based on the number of rows specified by the input `n`. The pattern should follow these rules:

- The first row has characters starting from `A` to `chr(65 + n - 1)` and then reverses back to `A`, with no spaces in between.
- Each subsequent row has increasing spaces in the middle, gradually replacing the characters, until only the first and last characters remain on the last row.

### **Input:**

- A single integer `n` (1 ≤ n ≤ 26), representing the number of rows to print.

### **Output:**

- A pattern printed as described.

### **Example:**

#### Input:

```plaintext
Enter Number of Rows: 5
```

#### Output:

```plaintext
A B C D E E D C B A
A B C D     D C B A
A B C         C B A
A B             B A
A                 A
```

### **Constraints:**

- The input `n` should be a positive integer between 1 and 26 (inclusive).

### **Note:**

Ensure that the pattern aligns properly, with spaces in the middle increasing by four spaces per row and the mirrored characters printed in reverse on the right-hand side.
