# 😂 Joke: "Why do programmers love printing patterns? Because they love to *see* the results! 🤓"

# Number of Rows
r = int(input("Enter Number of Rows: "))  # User input for the number of rows

# For Newline
print()  # Print a newline for spacing

# Printing Pattern
for i in range(r):  # Loop through each row from 0 to r-1

    # Determine the number of stars to print for the current row
    if (
        i <= r // 2
    ):  # If the current row is in the first half of the pyramid (including the center)
        val = 2 * i + 1  # Calculate the number of stars for the current row
    else:  # If the current row is in the second half (descending part)
        val = 2 * (r - i) - 1  # Calculate the number of stars in the descending part

    # Print the stars with a space in between
    print("* " * val)  # Print the star pattern for the current row
