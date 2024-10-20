### **Question: Memory Allocation in Structures**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Programming Languages (C)

**Input:**  
There is no input required from the user. The program assigns predefined values to the structure members and outputs the calculated sizes using the `sizeof` operator.

**Description:**
In this task, you are asked to determine the size of the individual members of a structure and the total size of the structure using the `sizeof` operator in C. The structure contains different data types, such as `int`, `float`, and `char[]`, each with its own memory requirements. Additionally, compilers may introduce padding bytes to optimize memory alignment.

### **Steps:**

1. **Define the Structure:**  
   A structure `student` is defined with the following members:

   - `gender`: a character array of size 10 (`char gender[10]`)
   - `rollno`: an integer (`int rollno`)
   - `marks`: a float (`float marks`)
   - `name`: a character array of size 20 (`char name[20]`)
   - `address`: a character array of size 30 (`char address[30]`)

2. **Initialize Structure Members:**
   In the `main` function, an object (or instance) of the `student` structure is created, and values are assigned to each of its members. String values are assigned using the `strcpy` function, while integer and float values are directly assigned.

3. **Print Member Values:**
   The values of each member (such as `rollno`, `marks`, `name`, etc.) are printed.

4. **Calculate Size Using `sizeof`:**
   The `sizeof` operator is applied to each structure member to calculate and print the size of each element (e.g., `sizeof(s1.rollno)`, `sizeof(s1.marks)`, etc.).

5. **Determine Total Structure Size:**
   Finally, the `sizeof` operator is applied to the entire structure (`sizeof(s1)`) to determine the total size of the structure, which includes padding added by the compiler.
