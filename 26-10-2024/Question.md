### **Question: Dutch National Flag Algorithm**

**Difficulty Level:** 🟡 Intermediate  
**Domain:** Algorithms and Data Structures (Sorting)

**Objective:**  
Given an array of integers representing colored balls (0 for red, 1 for white, and 2 for blue), arrange the elements so that all red balls (0s) come first, followed by white balls (1s), and then blue balls (2s), using a single pass through the array without extra space.

### **Conceptual Background:**

This problem, known as the Dutch National Flag problem, involves sorting an array of three distinct elements in a specific order. The algorithm is efficient, requiring a single traversal of the array with three main sections or "bins" in mind:

1. **Red Balls (0s):**

   - Imagine a "bin" at the beginning of the array. As you move through the array, any red balls encountered are "dropped" into this section, shifting other elements accordingly.

2. **White Balls (1s):**

   - In the middle of the array, white balls (1s) are left as they are. When a white ball is encountered, you simply move to the next element.

3. **Blue Balls (2s):**
   - At the end of the array is the blue section. When a blue ball is found, it’s moved to the end of the array without disturbing the order of red or white balls.

### **Steps to Approach:**

1. **Initialize Three Pointers:**

   - `low` to mark the position for red balls (0s).
   - `mid` for white balls (1s), starting from the beginning.
   - `high` for blue balls (2s), starting from the end of the array.

2. **Single Pass through the Array:**

   - Move `mid` through the array:
     - If it encounters a red ball (0), swap it with `low`, increment both `low` and `mid`.
     - If it encounters a white ball (1), just increment `mid`.
     - If it encounters a blue ball (2), swap it with `high` and decrement `high` without incrementing `mid`.

3. **Example Execution:**

   - **Initial Array:** [1, 0, 2, 1, 0, 2, 1, 0]
   - **Sorting in Progress:** The algorithm rearranges the array in a single pass to produce the sorted output `[0, 0, 0, 1, 1, 1, 2, 2]`.

By following this strategy, you will achieve the required sorted order in linear time and constant space, efficiently solving the Dutch National Flag problem.
