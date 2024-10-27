### Explanation

The Dutch National Flag problem efficiently sorts an array with only `0`s, `1`s, and `2`s in a single pass. Here's a short explanation of how it works:

1. **Setup**: We use three pointers:

   - `low` starts at the beginning of the array, pointing to where the next `0` should go.
   - `mid` also starts at the beginning, acting as the current pointer we evaluate.
   - `high` starts at the end, marking where the next `2` should go.

2. **Loop Through Array**:

   - As long as `mid` is less than or equal to `high`, evaluate the element at `arr[mid]`.

3. **Using Switch Cases**:

   - **If `arr[mid] == 0`**: Swap it with `arr[low]`, increment both `low` and `mid`. This ensures all `0`s are moved to the front.
   - **If `arr[mid] == 1`**: Simply move `mid` forward, as `1`s should stay in the middle.
   - **If `arr[mid] == 2`**: Swap `arr[mid]` with `arr[high]` and decrement `high`. Here, `mid` is not incremented because the swapped element needs checking.

4. **End Condition**:
   - The loop continues until `mid` goes beyond `high`.
   - The array is then sorted with all `0`s first, followed by `1`s, and then `2`s at the end.

This approach is efficient, achieving the sort in a single pass through the array.
