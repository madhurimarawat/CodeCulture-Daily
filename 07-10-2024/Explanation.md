### Explanation:

1. **Input Stage:**

   - The program starts by taking an integer input `n` from the user. This is the number we want to check if it's a perfect number or not.

2. **Divisor List Initialization:**

   - A list `positive_div` is initialized to store the positive divisors of the number `n`. Since 1 is a divisor of every number, it is automatically added to the list at the beginning.

3. **Finding Divisors:**

   - The loop iterates through numbers from `2` to `n//2`. Why `n//2`? Because no divisor (except the number itself) can be greater than half of the number.
   - For every value `i`, it checks if `i` divides `n` evenly (`n % i == 0`). If true, then `i` is a divisor and is added to the `positive_div` list.

4. **Sum Check:**
   - After finding all divisors, the program calculates the sum of all elements in the `positive_div` list using Python's `sum()` function.
   - If the sum of these divisors is equal to the original number `n`, the number is a **perfect number**, and the program prints `True`. Otherwise, it prints `False`.

### Example:

#### Input:

```python
Enter Number: 28
```

#### Output:

```python
True
```

Explanation:

- The divisors of 28 are: 1, 2, 4, 7, 14 (excluding 28 itself).
- The sum of these divisors is 28, which makes 28 a perfect number. Therefore, the program outputs `True`.
