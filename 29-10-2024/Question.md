### **Question: Unique Element Using XOR**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Algorithms and Data Structures (Bit Manipulation)

### **Objective:**

Given a sorted array where every element appears exactly twice except for one unique element that appears only once, identify this unique element. The task should be completed in **O(n)** time and **O(1)** space by leveraging the properties of the XOR operation.

### **Conceptual Background:**

The XOR operation has useful properties for identifying unique elements in arrays:
1. **XORing a number with itself** results in `0` (e.g., `a ^ a = 0`).
2. **XORing a number with `0`** retains the original number (e.g., `a ^ 0 = a`).

In an array where every element except one appears exactly twice, XORing all elements together will cancel out the pairs, leaving only the unique element.

### **Steps to Approach:**

1. **Initialize a Variable for XOR Accumulation:**
   Start with a variable, `unique_ele`, set to `0`.

2. **Traverse the Array Using XOR:**
   For each element in the array, apply the XOR operation between `unique_ele` and the element.
   
   - Each duplicate element pair will XOR to `0`, canceling each other out.
   - The unique element, which has no duplicate, will remain after all XOR operations.

3. **Return the Unique Element:**
   Once the loop completes, `unique_ele` will hold the value of the unique element.

### **Example Execution:**

- **Input:** `nums = [3, 3, 7, 7, 10, 11, 11]`
- **Processing:**
  - `unique_ele` is initialized to `0`.
  - Each element is XORed with `unique_ele`, cancelling paired elements.
  - The unique element remains after the XOR operations.
- **Output:** `10`

This approach is optimal in both time and space complexity, taking advantage of XOR’s properties to efficiently isolate the unique element in the array.
