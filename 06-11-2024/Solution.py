# Taking user input for an integer
n = int(input("Enter Integer: "))


# Defining function to convert an integer to its base 7 representation
def base_7(n):
    # If the number is 0, the string representation is "0"
    if n == 0:
        return "0"

    # Converting to absolute value for negative integers (handle negative separately)
    is_negative = n < 0
    n = abs(n)

    # Result string to store the base 7 representation
    res = ""

    # Loop to find the base 7 representation
    while n > 0:
        # Finding remainder when divided by 7
        rem = n % 7
        # Adding the remainder at the start of the result string
        res = str(rem) + res
        # Updating n by its integer division by 7
        n //= 7

    # If the original number was negative, prepend a minus sign
    if is_negative:
        res = "-" + res

    return res


# Calling the function and printing the result
print("Base 7 Conversion is:", base_7(n))
