### **Question: Alternating Number Pattern**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Pattern Printing

### **Objective:**

Generate a **descending pattern** of alternating numbers (1 and 0) based on a specified number of rows (`r`). The pattern should start with the number 1 in the first row and alternate between 1 and 0 in each subsequent row. Each row should contain one less element than the previous row until reaching a single element in the last row.

### **Requirements:**

1. **Pattern Specifications**:

   - **Input**: An integer `r` representing the number of rows.
   - **Output**: Print a pattern where:
     - **Odd rows** start with the number 1, and **even rows** with the number 0.
     - The first row contains `r` elements, the next row contains `r-1` elements, and so on, until the last row, which contains a single element.

2. **Example**:

   - **Input**: `5`
   - **Output**:
     ```
     1 1 1 1 1
     0 0 0 0
     1 1 1
     0 0
     1
     ```

3. **Solution Structure**:
   - **Loop** through each row, starting with `r` elements and decrementing the count in each row.
   - **Alternate** between printing `1` and `0` by checking whether the current row is odd or even.

### **Guidelines**:

- Ensure that the pattern alternates correctly and maintains a clear descending structure.
- Test with different values of `r` to confirm that the solution works as expected.
