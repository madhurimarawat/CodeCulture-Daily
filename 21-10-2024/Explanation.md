## **Half Pyramid Pattern Program in C**

## **Program Overview**

This program takes an integer input `n` from the user and prints a half-pyramid pattern made of stars (`*`) up to `n` rows. The number of stars increases progressively in each row, starting from 1 star in the first row and going up to `n` stars in the last row.

## **How the Program Works**

### **1. Taking Input**

The program prompts the user to enter the number of rows for the pyramid (`n`):

```c
printf("Enter number of Rows: ");
scanf("%d", &n);
```

Here, `scanf()` is used to store the input value of `n`.

### **2. Printing the Half Pyramid**

The program uses two nested `for` loops to print the half-pyramid pattern:

```c
for(int i = 0; i <= n; i++) {
    for(int j = 0; j < i; j++) {
        printf("* ");
    }
    printf("\n");
}
```

- **Outer Loop (`i`)**: Controls the number of rows to print. It runs from 0 to `n`, where `n` is the number of rows specified by the user.
- **Inner Loop (`j`)**: Controls how many stars are printed on each row. For each row `i`, the inner loop prints `i` stars.
- After printing all the stars on the current row, a new line (`\n`) is printed to move to the next row.

### **3. Example Execution**

If the user enters `n = 4`, the output will be:

```
*
* *
* * *
* * * *
```

## **Key Points**

- The number of stars printed in each row is equal to the current row number (`i`).
- The program uses `printf()` to print each star followed by a space (`* `).
- After printing all stars in a row, the `printf("\n")` statement moves the cursor to the next line.
