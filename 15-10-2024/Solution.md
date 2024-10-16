### **Solution: Code Formatting Tools for C and C++**

#### Tools Overview

1. **Online Tool: [CodeBeautify](https://codebeautify.org/cpp-formatter-beautifier)**

   - Automatically formats the code once pasted. Ideal for 1-2 files.
   - Paste the code and get instant formatted output.

2. **System Tool: Astyle (Artistic Style)**
   - Best for multiple files in larger projects, allowing batch processing.
   - Use Astyle to format code with one command for all files.

---

#### **Steps for Using Astyle**

For detailed installation steps and command descriptions, refer to [Astyle Commands Documentation](https://madhurimarawat.github.io/Semester-Notes/Astyle-Commands.html).

1. **Installation:**

   - **Windows (Using Chocolatey)**:

     ```powershell
     choco install astyle
     ```

   - **Linux**:

     ```bash
     sudo apt-get install astyle
     ```

   - **macOS**:
     ```bash
     brew install astyle
     ```

2. **Usage Example:**

   To format a file:

   ```bash
   astyle filename.c
   ```

   For batch formatting:

   ```bash
   astyle *.c *.cpp
   ```

3. **Customizing Format** (e.g., Allman style with 4 spaces):
   ```bash
   astyle --style=allman --indent=spaces=4 *.c *.cpp
   ```

---

#### **When to Use Which Tool?**

- **CodeBeautify**: Quick formatting for small files (1-2 files).
- **Astyle**: Efficient for multiple files, offering batch processing with customizable formatting options.
