### **Question: Row Typability Challenge**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Algorithms and Data Structures (String Processing)

**Objective:**  
Given a list of words, return only those words that can be typed using letters from a single row of an American keyboard layout.

### **Conceptual Background:**

In this challenge, the goal is to identify words that can be typed using letters from only one row on a standard QWERTY keyboard. American keyboards generally have the following layout:

- **Top row:** QWERTYUIOP
- **Middle row:** ASDFGHJKL
- **Bottom row:** ZXCVBNM

To solve this problem, the code must:

1. Verify which row each word belongs to by checking if all letters of the word are contained within the letters of one row.
2. Return only the words that meet the requirement of being typed using one row.

### **Steps to Approach:**

1. **Convert Each Word to Uppercase:**  
   The keyboard rows are typically represented in uppercase letters, so each word is converted to uppercase to ensure case-insensitive comparison.

2. **Check if Word is Row Typable:**  
   For each word, determine if all characters exist within a single keyboard row:

   - Use a loop to check if every letter in the word exists in any one of the rows.
   - If a word meets this criterion, it is considered "row typable" and added to the output list.

3. **Output Row Typable Words:**  
   The result will include all words that can be typed with letters from only one row on the keyboard.

### **Example Execution:**

- **Input:** `["Hello", "Alaska", "Dad", "Peace"]`
- **Processing:**
  - **"Hello"** - Letters exist across multiple rows, so it is excluded.
  - **"Alaska"** - All letters exist in the middle row.
  - **"Dad"** - All letters exist in the middle row.
  - **"Peace"** - Letters exist across multiple rows, so it is excluded.
- **Output:** `["Alaska", "Dad"]`

The solution efficiently checks for each word, making it an effective approach for this string-processing task.
