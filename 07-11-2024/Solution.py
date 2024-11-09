# Number of Rows
r = int(
    input("Enter Number of Rows: ")
)  # Taking user input for the number of rows in the pattern

# For Newline
print()  # Print a newline for better formatting before starting the pattern

# Printing Pattern
for i in range(r, 0, -1):  # Loop to control the number of rows, starting from 'r' to 1

    mid = 2 * i // 2  # Calculate the midpoint of characters in the current row

    for j in range(2 * i):  # Loop to print characters in each row, up to 2*i columns

        # Check if the column index is in the first half of the pattern
        if j < mid:
            print(chr(j + 65), end=" ")  # Print alphabet characters from 'A' onwards

        # If the column index is in the second half of the pattern
        else:
            print(
                chr(2 * mid - j + 64), end=" "
            )  # Print the mirrored character in reverse

    print()  # Move to the next line after printing all columns in the current row
