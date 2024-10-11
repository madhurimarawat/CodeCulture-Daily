# Zigzag Matrix Traversal

## Introduction:
In this solution, we will traverse a 2D matrix in a zigzag manner, which means:
- The first row is traversed from left to right.
- The middle rows are traversed from right to left.
- The last row is traversed from left to right.

This creates a pattern where the traversal direction alternates between rows.

## Explanation:

### 1. Input Matrix:
We start by creating a matrix using the `numpy` library. There's a function called `input_matrix()` which takes user input for the matrix. For simplicity, in the sample code, we've used a predefined 3x3 matrix.

### 2. Zigzag Traversal:
The main function `zigzag_order_mat()` performs the zigzag traversal. It follows these steps:
- If the current row is the first or last row, traverse from left to right.
- If the current row is a middle row, traverse from right to left.
  
The result is stored in a list and returned to be printed.

### Sample Input and Output:

**Input Matrix:**
```
1  2  3
4  5  6
7  8  9
```

**Zigzag Traversal:**
```
[1, 2, 3, 6, 5, 4, 7, 8, 9]
```

This zigzag traversal captures the first and last rows in a normal order, while the middle row is reversed.

## Key Functions:
- `input_matrix()`: Takes user input for the matrix.
- `zigzag_order_mat()`: Traverses the matrix in a zigzag manner and returns the result.

## Conclusion:
This is an efficient and simple approach to achieve a zigzag traversal of a matrix. The time complexity is O(m * n), where `m` is the number of rows and `n` is the number of columns.
