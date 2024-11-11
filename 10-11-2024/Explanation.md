#### Program Explanation:

**Why do arrays never get lost?**  
👉 **Answer**: Because they always have an _index_ to find their way! 😆🔢

This program finds the _next greater element_ for each element in `nums1` from `nums2`. Here’s a detailed explanation:

1. **Input Handling**:

   - The program takes input for `nums1` and `nums2` as space-separated integers.
   - These inputs are converted into lists of integers for processing.

2. **Logic to Find Next Greater Element**:

   - For each element in `nums1`, the program looks for the next greater element in `nums2` starting from the position right after the current element's index.
   - If a greater element is found, it is added to the result list (`res`).
   - If no greater element is found, `-1` is added to `res`.

3. **Nested Loop Explanation**:

   - The outer loop iterates over each element in `nums1`.
   - The inner loop starts from the next index of the current element in `nums2` and searches for the next greater element.

4. **Output**:
   - The result list is printed, showing the next greater element for each item in `nums1` or `-1` if none exists.

---

### Example Execution:

**Input:**

```plaintext
Enter elements for nums1 separated by space: 4 1 2
Enter elements for nums2 separated by space: 1 3 4 2
```

**Output:**

```plaintext
Next greater elements for nums1 in nums2: [-1, 3, -1]
```
