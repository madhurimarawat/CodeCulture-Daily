# "Humans may not be perfect, but at least numbers can be! 😄"

# Taking Input from the user for a number
n = int(input("Enter Number: "))

# Initializing a list to store positive divisors of the number
# Adding 1 to the list because 1 is a positive divisor for all numbers
positive_div = [1]

# Finding all positive divisors of the number except the number itself
# We only need to check divisors up to n//2 because any number's divisors (excluding itself)
# will always be less than or equal to half of that number.
for i in range(2, n // 2 + 1):

    # If 'i' divides 'n' evenly (i.e., remainder is 0), it is a divisor
    if n % i == 0:
        positive_div.append(i)  # Add the divisor to the list

# Checking if the sum of the divisors equals the original number
# The sum() function is used to get the total of the divisors in the list
if n == sum(positive_div):
    print("True")  # The number is perfect
else:
    print("False")  # The number is not perfect
