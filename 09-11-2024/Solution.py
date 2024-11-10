# Number of Rows
r = int(input("Enter Number of Rows: "))  # Taking user input for the number of rows

# For Newline
print()  # Print a newline for better formatting before starting the pattern

# Printing Pattern
for i in range(r):  # Loop to control the number of rows, starting from 0 to r-1

    # For Decreasing Pattern
    for j in range(
        i, 0, -1
    ):  # Loop to print numbers in decreasing order starting from 'i' down to 1
        print(j, end=" ")  # Print the current value of 'j' with a space

    # For Increasing Pattern
    for j in range(i + 1):  # Loop to print numbers in increasing order from 0 to 'i'
        print(j, end=" ")  # Print the current value of 'j' with a space

    print()  # Move to the next line after printing all columns in the current row
