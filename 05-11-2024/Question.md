### **Question: Increasing Letter Pattern**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Pattern Printing

### **Objective:**

Generate an **increasing pattern** of letters, where each row starts with the letter 'A' and each subsequent row continues with the next letter in alphabetical order. The number of letters in each row should match the row number, starting from 1.

### **Requirements:**

1. **Pattern Specifications**:

   - **Input**: An integer `r` representing the number of rows.
   - **Output**: Print a pattern where:
     - The first row contains the letter 'A' repeated once.
     - The second row contains the letter 'B' repeated twice.
     - This pattern continues, with each row containing the next letter and the count of the letter matching the row number, until reaching `r` rows.

2. **Example**:

   - **Input**: `5`
   - **Output**:
     ```
     A
     B B
     C C C
     D D D D
     E E E E E
     ```

3. **Solution Structure**:
   - **Loop** through each row, starting from 1 up to `r`.
   - For each row, **calculate** the appropriate letter by starting from 'A' and shifting by the row number.
   - **Repeat** the letter for the current row number times to form the pattern.

### **Guidelines**:

- Make sure the pattern increments the letters correctly and aligns each row properly.
- Test with various values of `r` to ensure correct letter and row count in the output.
