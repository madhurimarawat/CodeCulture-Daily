# Taking Input from the user for the size of the array
N = int(input("Enter Number of Elements: "))

# Initializing an empty list to store the array elements
circular_array = []

# Loop to take inputs for each element in the circular array
for i in range(N):
    ele = int(input(f"Enter Element {i+1}: "))  # Take each element from user
    circular_array.append(ele)  # Append each element to the array list

# Function to find the next greater element for each item in the circular array
def next_greater_element(circular_array):

    # Initialize a list to store the next greater elements for each item
    next_greater_ele = []

    # Outer loop: iterate over each element in the array
    for i in range(N):

        # Initialize a variable to store the next greater element, set to -1 by default
        next_greater = -1  # Default value if no greater element is found

        # Inner loop: Check each element circularly for a greater number
        for j in range(1, N):  # Start from the next element up to the end

            # Calculate the circular index using modulo
            index = (i + j) % N

            # Check if the element at the circular index is greater
            if circular_array[index] > circular_array[i]:
                next_greater = circular_array[index]  # Update the next greater element
                break  # Exit the loop once the next greater element is found

        # Append the found next greater element to the result list
        next_greater_ele.append(next_greater)

    # Return the list of next greater elements for the entire array
    return next_greater_ele

# Display the result
print("Next Greater Number in Circular Array is:")
# Call the function and print the next greater elements
print(next_greater_element(circular_array))
