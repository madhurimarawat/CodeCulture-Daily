### **Solution: Markdown to PDF Conversion**

To convert Markdown to PDF, we can utilize both online tools and local software. Here’s how to set up and use these tools effectively.

#### **Online Tools**

1. **md2pdf**:
   - A straightforward online tool for converting Markdown to PDF, accessible [here](https://md2pdf.netlify.app/).
   - **Advantages**: Quick and easy to use; highlights important keywords in commands like `SELECT` and `JOIN`.
   - **Disadvantages**: Does not handle wide tables well (horizontally large tables are cut off).
2. **Markdown to PDF**:
   - Another user-friendly online converter, accessible [here](https://www.markdowntopdf.com/). Note that after one conversion, login is required, and three conversions are allowed before requiring a premium account.
   - **Advantages**: Handles horizontally large tables well; layout is similar to GitHub’s Markdown preview.
   - **Disadvantages**: No syntax highlighting for code; limited free usage without an account. Lacks color support for commands (no syntax highlighting for code blocks or keywords).

#### **Local Tools Setup**

For local conversion, we can use **Pandoc** and **wkhtmltopdf** for more flexibility and control over the output.

##### **1. Download and Install Pandoc**:

- Visit the [Pandoc GitHub Releases Page](https://github.com/jgm/pandoc/releases/tag/3.5) and download the appropriate ZIP file for your operating system.
- Unzip the file and move the contents to a folder named **Pandoc** in **C:\Program Files** (for Windows users).

##### **2. Download and Install wkhtmltopdf**:

- Go to the [wkhtmltopdf Download Page](https://wkhtmltopdf.org/downloads.html) and download the version suitable for your system.
- Run the installer to set it up.

##### **3. Set Up System Environment Variables**:

- Right-click on **This PC** (or **My Computer**) and select **Properties**.
- Click on **Advanced system settings**.
- In the **System Properties** window, go to the **Environment Variables** section.
- Under **System variables**, find the **Path** variable and click on **Edit**.
- Add the following paths to the list (adjust if the installation paths differ):
  - `C:\Program Files\Pandoc`
  - `C:\Program Files\wkhtmltopdf\bin`

##### **4. Convert Markdown to PDF Using Pandoc**:

Once everything is set up, you can use Pandoc to convert Markdown files to PDF. Here’s the basic command:

```bash
pandoc filename.md -o filename.pdf --pdf-engine=wkhtmltopdf
```

Replace `filename.md` with your Markdown file and `filename.pdf` with the desired output name.

##### **Handling Margins**:

By default, Pandoc’s PDF conversion can have large margins. To adjust them, you can add options to customize the margins and page layout:

```bash
pandoc filename.md -o filename.pdf --pdf-engine=wkhtmltopdf --variable geometry:margin=1in
```

This command sets the margin to 1 inch. You can adjust the margin size as needed.

You can also specify more advanced layout options like paper size, font size, and margins:

```bash
pandoc filename.md -o filename.pdf --pdf-engine=wkhtmltopdf --variable geometry:margin=1in,paper=a4 --variable fontsize=12pt
```

### **Advantages and Disadvantages**

#### **Online Tools**:

- **Advantages**:
  - Easy to use, no installation required.
  - Ideal for simple or quick conversions.
  - Some tools like Markdown to PDF handle wide tables well.
- **Disadvantages**:
  - Limited functionality for larger or more complex files (e.g., wide tables, syntax highlighting).
  - Often requires an account or has usage limits (Markdown to PDF, for example).
  - Minimal control over margins, layout, or PDF customization.

#### **Local Tools (Pandoc & wkhtmltopdf)**:

- **Advantages**:

  - Full control over the PDF output (margins, layout, paper size, font size).
  - Handles complex Markdown files, large tables, and custom styles.
  - No usage limits; ideal for frequent conversions.

- **Disadvantages**:
  - Initial setup is required (installing and configuring Pandoc, wkhtmltopdf, and environment variables).
  - Involves command-line usage, which can be less user-friendly for beginners.
