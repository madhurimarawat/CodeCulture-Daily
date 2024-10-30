### Explanation:

**"Why is the unique element eternally single?**  
Because everyone else found their perfect match, leaving it to go solo forever!" 😂

Given the array `nums = [3, 3, 7, 7, 10, 11, 11]`:

1. **Initialization:** `unique_ele = 0`

2. **XOR Process:**

   - `0 ^ 3 = 3` → (`unique_ele = 3`)
   - `3 ^ 3 = 0` → (`unique_ele = 0`, 3s cancel out)
   - `0 ^ 7 = 7` → (`unique_ele = 7`)
   - `7 ^ 7 = 0` → (`unique_ele = 0`, 7s cancel out)
   - `0 ^ 10 = 10` → (`unique_ele = 10`)
   - `10 ^ 11 = 1` → (`unique_ele = 1`)
   - `1 ^ 11 = 10` → (`unique_ele = 10`, 11s cancel out)

3. **Result:**
   - After the XOR operation on all elements, `unique_ele` contains `10`, which is the unique element in the array.

### **Summary:**

By using the XOR operation on each element in the array, we efficiently cancel out pairs of identical elements, leaving only the single, unique element. This approach allows the solution to run in linear time with constant space.
