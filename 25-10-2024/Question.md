### **Question: Exploring the `auto` Keyword in C++**

**Difficulty Level:** 🟢 Beginner  
**Domain:** Programming Languages (C++)

**Objective:**  
Write a C++ program to demonstrate the `auto` keyword’s ability to automatically infer the type of variables. This program will declare variables with initial values without specifying their types explicitly, and the compiler will deduce the appropriate type based on these initial values. The program will then output each variable's inferred type to verify the deduced types.

### **Detailed Description:**

In C++, the `auto` keyword provides a way to simplify variable declarations by enabling the compiler to automatically determine a variable's type from the value assigned to it. This can make the code cleaner, especially when working with complex or unfamiliar types, and reduces the risk of errors when explicitly specifying types.

### **Instructions for the Program:**

1. **Declare Variables Using `auto`:**

   - Define several variables with different types of values (e.g., an integer, a floating-point number, and a string). Instead of specifying types like `int`, `double`, or `const char*`, use `auto` as the type.
   - The compiler will deduce:
     - `int` for integer values
     - `double` for floating-point numbers
     - `const char*` for string literals

2. **Display the Deduced Types:**

   - Use `typeid(variable).name()` to print the inferred type of each variable, which will appear in shorthand form:
     - `i` represents the integer type.
     - `d` represents the double type.
     - `PKc` represents a constant character pointer (`const char*`), commonly used for strings.
   - This step confirms that the compiler correctly inferred each variable’s type based on its initial value, showcasing how `auto` makes the code both concise and accurate without explicit type declarations.

3. **Expected Output:**
   - The output should display the inferred types of each variable, using the internal representations produced by `typeid`, allowing you to see how `auto` has successfully deduced each type.
