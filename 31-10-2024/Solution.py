# Number of Rows
try:
    r = int(input("Enter Number of Rows: "))

    # List of diyas
    diyas = ["🔴", "🟡", "⚪", "🟢", "🔵"]

    print()

    # Loop to Print Pattern
    for i in range(0, r):
        for j in range(0, r):
            print(diyas[(i + j) % len(diyas)], end=" ")
        print()

except ValueError:
    print("Please enter a valid integer for the number of rows.")
