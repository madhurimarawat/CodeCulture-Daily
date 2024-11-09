# Taking user input for the number of rows in the pattern
r = int(input("Enter Number of Rows: "))

# For Newline to format the output
print()

# The ASCII value of the starting character ('A')
start = ord("A")

# The ASCII value of the ending character, calculated based on user input
end = start + r

# Loop to iterate over the range of ASCII values from 'A' to the calculated end character
for i in range(start, end):
    # Print the character corresponding to the ASCII value `i`, repeated as needed
    # (i + 1 - 65) ensures that 'A' is printed once, 'B' twice, etc.
    print(chr(i) * (i + 1 - 65))
