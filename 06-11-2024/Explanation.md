# Explanation of Base 7 Conversion

**Why was the number 7 afraid of the conversion? Because it kept dividing until it couldn't take any more! 😅➗7➡️202**

## Overview

The code converts an integer to its base 7 representation. This process involves dividing the number repeatedly by 7 and recording the remainders.

### Example Step-by-Step Conversion of 100 to Base 7

1. **First Division**:

   - 100 ÷ 7 = 14, remainder **2**.
   - Remainder is added to the result.

2. **Second Division**:

   - 14 ÷ 7 = 2, remainder **0**.
   - Remainder is added to the start of the result.

3. **Third Division**:

   - 2 ÷ 7 = 0, remainder **2**.
   - Remainder is added to the start of the result.

4. **Result**:
   - Since we reached 0, we stop dividing.
   - The remainders collected in reverse order form the base 7 representation.
   - **The base 7 representation of 100 is "202".**

## Negative Number Handling

- If the input is negative, the code converts it to its absolute value for processing.
- After conversion, a minus sign is prepended to the result to indicate the negative value.

## Key Points

- The `while` loop continues until `n` becomes 0.
- The division by 7 gives the next quotient to use in the loop.
- The modulo operation (`n % 7`) finds the remainder for each digit in the base 7 system.

By adjusting the division for any base (changing the `7` to another base), you can reuse the same logic for different base conversions.
