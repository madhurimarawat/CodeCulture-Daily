#### Program Explanation

**Why did the number pattern break up with the alphabet pattern?**  
👉 **Answer**: Because it just couldn't handle all those letters getting in its _sequence_! 🤣📝

This code generates a numerical pattern where each row displays a combination of decreasing and increasing sequences. Here's a detailed breakdown:

1. **Input**:

   - The user is prompted to input the number of rows (`r`).

2. **Outer Loop**:

   - The `for` loop iterates from `0` to `r-1`, controlling the number of rows to be printed.

3. **Decreasing Pattern**:

   - The first `for` loop prints numbers in decreasing order starting from the current row index (`i`) down to `1`.

4. **Increasing Pattern**:

   - The second `for` loop prints numbers in increasing order from `0` up to the current row index (`i`).

5. **Output**:
   - The result is a symmetrical numerical pattern, with each row containing numbers that first decrease and then increase.

---

### Example Output

For an input of `r = 5`, the output would look like:

```
0
1 0 1
2 1 0 1 2
3 2 1 0 1 2 3
4 3 2 1 0 1 2 3 4
```
