# Given sorted array where every element appears exactly twice except one unique element
nums = [3, 3, 7, 7, 10, 11, 11]


def unique_element(arr):
    # Initialize unique_ele to 0 since XOR with 0 retains the other number.
    # XOR of two identical numbers results in 0, while XOR of a number with 0 retains the number.
    # By XORing all elements, we eliminate paired numbers and are left with the unique number.
    unique_ele = 0

    # Traverse through each element in the array
    for i in range(len(arr)):
        # XOR the current element with unique_ele.
        # This effectively "cancels out" pairs of identical numbers
        # and accumulates the unique number in unique_ele.
        unique_ele = unique_ele ^ arr[i]

    # After the loop completes, unique_ele will hold the single element
    return unique_ele


# Print the result, which is the unique element in the array
print("Unique Number is:", unique_element(nums))
