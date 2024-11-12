# Initialize an empty list to store the array elements
nums = []

# Accept input from the user as a space-separated string and convert to integers
nums_input = input("Enter the elements of the array (0s and 1s, space-separated): ")
nums = [int(x) for x in nums_input.split()]

# Variable to store the maximum length of subarray found
max_len = 0

# Loop through each element as the starting index of the subarray
for i in range(len(nums)):
    # Initialize counters for 0s and 1s
    count_0, count_1 = 0, 0

    # Inner loop to count 0s and 1s up to the current index `i`
    for j in range(i + 1):
        if nums[j] == 0:
            count_0 += 1  # Increment count for 0s
        else:
            count_1 += 1  # Increment count for 1s

    # Check if the number of 0s and 1s are equal
    if count_0 == count_1:
        current_length = i + 1  # Calculate the current length

        # Update the maximum length if the current one is greater
        if current_length > max_len:
            max_len = current_length

# Print the result: the length of the longest contiguous subarray
print("The maximum length of contiguous subarray with equal 0s and 1s is:", max_len)
