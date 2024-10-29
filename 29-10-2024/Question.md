### **Question: Unique Element**

**Difficulty Level:** 🟡 Intermediate  
**Domain:** Algorithms and Data Structures (Binary Search)

### **Objective:**

Given a sorted array where every element appears exactly twice except for one unique element that appears only once, identify this unique element. The challenge requires achieving this in **O(log n)** time and **O(1)** space.

### **Conceptual Background:**

The array is sorted and every element except one appears in pairs, allowing the unique element to be located efficiently with a binary search approach. Since binary search works well with sorted data and can achieve logarithmic time complexity, it's a suitable technique here.

### **Steps to Approach:**

1. **Binary Search Setup:**  
   Initialize two pointers, `left` and `right`, representing the bounds of the search range.

2. **Binary Search to Locate Unique Element:**  
   Perform binary search:

   - Calculate the midpoint `mid`.
   - Determine if the midpoint index is even or odd.
   - If `nums[mid]` equals `nums[mid + 1]` or `nums[mid - 1]`, the unique element is located further to the right or left respectively.

3. **Narrowing Down the Search:**  
   Adjust `left` and `right` pointers based on comparisons to ensure you converge towards the unique element efficiently. This process will conclude with the unique element at the `left` pointer once the range is narrowed down.

4. **Output the Unique Element:**  
   Once found, the element at the `left` pointer is the unique element in the array.

### **Example Execution:**

- **Input:** `nums = [3,3,7,7,10,11,11]`
- **Processing:**
  - Binary search will adjust `left` and `right` pointers based on the pairing position.
  - As the binary search narrows down, it isolates the unique element.
- **Output:** `10`

This approach, leveraging binary search, ensures the solution runs in optimal time and space complexity.
