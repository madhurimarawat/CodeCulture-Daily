### **Question: Code Formatting Tools for C and C++ Files**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Tools and Technology

**Description:**  
Code formatting tools for C and C++ help enforce consistent style, improve readability, and maintain clean code. These tools automatically adjust spacing, indentation, and braces for both C and C++ files according to industry standards or user-defined rules. This task involves finding reliable formatting tools, either online or locally, that can process C and C++ code.

**Input Example:**

**filename.c:**

```c
#include<stdio.h>
int main() {
int a=10;
if(a>5){
printf("A is greater than 5");
}
return 0;
}
```

**filename.cpp:**

```cpp
#include<iostream>
using namespace std;
int main() {
int b=20;
if(b<30){
cout<<"B is less than 30";
}
return 0;
}
```

**Output Example:**

**Formatted filename.c:**

```c
#include <stdio.h>

int main() {
    int a = 10;
    if (a > 5) {
        printf("A is greater than 5");
    }
    return 0;
}
```

**Formatted filename.cpp:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int b = 20;
    if (b < 30) {
        cout << "B is less than 30";
    }
    return 0;
}
```
