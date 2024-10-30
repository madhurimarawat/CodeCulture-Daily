### **Question: Capital Usage Validator**

**Difficulty Level:** 🟢 Beginner  
**Domain:** String Processing (Validation)

### **Objective:**

Given a word, determine if its capitalization is used correctly. We define correct capitalization as follows:

1. All letters in the word are uppercase (e.g., `"USA"`).
2. All letters in the word are lowercase (e.g., `"leetcode"`).
3. Only the first letter in the word is uppercase (e.g., `"Google"`).

If any of these conditions are met, return `True`. Otherwise, return `False`.

### **Conceptual Background:**

To validate correct capitalization, we simply need to check three conditions for the input word:

1. **All Uppercase:** Every letter in the word is capital.
2. **All Lowercase:** Every letter in the word is lowercase.
3. **Title Case:** Only the first letter is uppercase, and all other letters are lowercase.

Python provides straightforward string methods (`isupper`, `islower`, and `istitle`) to evaluate each of these cases, allowing for an efficient solution.

### **Example Execution:**

- **Input:** `"USA"`
- **Processing:**
  - `isupper()` returns `True` because all letters are uppercase.
  - Since one condition is satisfied, the function returns `True`.
- **Output:** `True`

- **Input:** `"Google"`
- **Processing:**
  - `istitle()` returns `True` since only the first letter is uppercase.
  - The function returns `True`.
- **Output:** `True`

- **Input:** `"flaG"`
- **Processing:**
  - None of the conditions (`isupper`, `islower`, `istitle`) are satisfied.
  - The function returns `False`.
- **Output:** `False`
