# Number of Rows
r = int(input("Enter Number of Rows: "))  # Prompt the user to input the number of rows

# For Newline
print()  # Print a newline to separate input from output

# Printing Pattern
for i in range(
    r, 0, -1
):  # Start from the total number of rows `r` and decrement down to 1
    if i % 2 == 0:  # Check if the current row number is even
        print("0 " * i)  # If even, print '0' repeated `i` times
    else:  # For odd rows
        print("1 " * i)  # Print '1' repeated `i` times
