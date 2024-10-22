### **Explanation of Memory Size:**

1. **Size of Individual Members:**

   - `char gender[10]`: 10 bytes (1 byte per character)
   - `int rollno`: 4 bytes (typically)
   - `float marks`: 4 bytes
   - `char name[20]`: 20 bytes
   - `char address[30]`: 30 bytes

   Total size without padding: 10 + 4 + 4 + 20 + 30 = 68 bytes

2. **Padding and Alignment:**
   Depending on the system architecture (e.g., 32-bit or 64-bit), compilers add padding to align data in memory. In this case, with padding, the total size of the structure is 72 bytes.

3. **Conclusion:**
   The size of a structure depends not only on the size of its members but also on memory alignment and padding introduced by the compiler.
