### **Question: Find the Next Greater Element in Array**

**Difficulty Level:** 🟡 Intermediate  
**Domain:** Arrays and Searching

### **Objective:**

Create a program that finds the next greater element for each element in a given subset array from its corresponding positions in a larger array.

### **Problem Description:**

You are given two arrays `nums1` and `nums2` without duplicates, where `nums1` is a subset of `nums2`. Your task is to find the _Next Greater Number_ for each element in `nums1` from `nums2`.

- The _Next Greater Number_ for an element `x` in `nums1` is the first greater number to the right of `x` in `nums2`.
- If no greater number exists for an element, return `-1`.

### **Input:**

- Two arrays:
  - `nums1` (1 ≤ length ≤ 1000) — a subset of `nums2`.
  - `nums2` (1 ≤ length ≤ 1000) — an array containing distinct integers.

### **Output:**

- An array of integers representing the next greater number for each element in `nums1` based on its position in `nums2`.

### **Example:**

#### Input:

```plaintext
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
```

#### Output:

```plaintext
[-1, 3, -1]
```

#### Explanation:

- For `4` in `nums1`, there is no greater number to its right in `nums2`, so the output is `-1`.
- For `1` in `nums1`, the next greater number in `nums2` is `3`.
- For `2` in `nums1`, there is no greater number to its right in `nums2`, so the output is `-1`.

### **Constraints:**

- All elements in `nums1` and `nums2` are distinct.
- The length of `nums1` will always be less than or equal to `nums2`.

### **Note:**

Make sure to optimize your solution to handle the maximum length efficiently and output the results in the same order as `nums1`.
