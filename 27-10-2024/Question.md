### **Question: Next Greater Number in a Circular Array**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Algorithms and Data Structures (Arrays)

**Objective:**  
Given a circular array of integers, the goal is to find the Next Greater Number for each element. The Next Greater Number for an element `x` is the first greater number that appears in a circular traversal after `x`. If no such greater number exists, output `-1` for that position.

### **Conceptual Background:**

In a regular array, the Next Greater Number of an element is simply the first number that is larger and appears later in the array. However, in a circular array, the end of the array "wraps around" to connect with the start, so every element effectively has both "next" and "previous" neighbors.

### **Steps to Approach:**

1. **Traverse the Array Circularly:**

   - The challenge is to check each element for the next greater number in a way that continues from the end back to the start of the array.

2. **Using a Stack for Efficiency:**

   - To make the solution efficient, we use a stack that keeps track of indices of elements. This helps us maintain the order and quickly find the next greater element.
   - By iterating twice over the array length (to handle the circular aspect), we ensure each element is evaluated thoroughly.

3. **Example Execution:**

   - **Input:** `[1, 2, 1]`
   - **Output Explanation:**

     - For the first element `1`, the next greater number in the circular array is `2`.
     - For the second element `2`, there is no greater number after it, so the output is `-1`.
     - For the last element `1`, wrapping around the array, the next greater number is `2`.

   - **Output:** `[2, -1, 2]`

This problem helps build foundational skills in understanding array traversal techniques, stack usage, and the concept of circular arrays in algorithm design.
