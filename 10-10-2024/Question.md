### **Question: Matrix Zigzag Order**

**Difficulty Level:** 🟡 Intermediate  
**Domain:** Data Structures (2D Arrays)

**Description:**  
Given an M x N matrix, return all the elements in Zigzag order. The zigzag traversal moves right across a row, down a column, and alternates directions when moving from row to row.

**Input Example:**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Output Example:**

```python
Zigzag Order: [1, 2, 3, 6, 5, 4, 7, 8, 9]
```

**Instructions:**

1. Implement a function to traverse the matrix in a zigzag pattern.
2. The function should:
   - Start from the top-left corner of the matrix.
   - Move left-to-right, then right-to-left alternately as it moves down each row.
3. Ensure that the traversal works for any M x N matrix.
4. The solution can be implemented in any programming language (Python, C++, Java, etc.).
