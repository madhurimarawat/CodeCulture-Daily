### **Question.md: Output of C Code**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Programming Languages (C)

**Description:**  
The following C program utilizes a `do-while` loop and an `enum` to define boolean values. The task is to determine the output produced when the code is executed. The `do-while` loop will run once, as the `while` condition is set to `false`. The code increments the variable `i` within the loop, but due to the `continue` statement and the `false` condition, the loop will terminate after the first iteration.

**Input:**  
No input is provided to the program, as the output is based on hardcoded logic in the code.

```c
#include<stdio.h>
#include<stdlib.h>

enum{false, true};

int main(){

    int i = 1;

    do {
        printf("%d\n", i);
        i++;

        if (i < 15)
            continue;

    } while(false);

    getchar();

    return 0;
}
```

**Output:**  
Choose the correct output based on the code provided.

1. 2
2. 1
3. 4
4. 3
