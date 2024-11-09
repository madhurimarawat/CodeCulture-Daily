### **Question: Pyramid Pattern Printing**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Patterns and Loops

### **Objective:**

Create a program that prints a symmetric pyramid pattern using stars (`*`) based on a given integer input `n`.

### **Problem Description:**

Given an integer input `n`, print a pyramid pattern following these rules:

1. **Base Element (Row 1):** The pattern starts with a single `*` at the center.
2. **Symmetric Expansion (Rows 2 and Beyond):** Each subsequent row symmetrically adds more `*` symbols, expanding to form a pyramid shape. After reaching the widest part, the pattern shrinks symmetrically to match the top part.
3. **Structured Array:** The pyramid pattern consists of `*` symbols arranged in a visually balanced structure.

### **Input:**

- A single integer `n` (1 ≤ n ≤ 20), representing the number of rows up to the widest part of the pyramid.

### **Output:**

- A pyramid pattern printed as described.

### **Example:**

#### Input:

```plaintext
Enter Number of Rows: 3
```

#### Output:

```plaintext
*
* * *
* * * * *
* * *
*
```

### **Constraints:**

- The input `n` should be a positive integer between 1 and 20 (inclusive).

### **Note:**

Ensure that the `*` symbols align symmetrically and each row centers appropriately.
