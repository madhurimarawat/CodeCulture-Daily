# Declaring Two Arrays
nums1, nums2 = [], []  # Initialize empty lists for nums1 and nums2

# Input for nums1
nums1_input = input("Enter elements for nums1 separated by space: ")
# Convert the input string into a list of integers
nums1 = [int(x) for x in nums1_input.split()]

# Input for nums2
nums2_input = input("Enter elements for nums2 separated by space: ")
# Convert the input string into a list of integers
nums2 = [int(x) for x in nums2_input.split()]

# Result list to store the next greater elements
res = []

# Loop through each element in nums1
for i in range(len(nums1)):
    found = False  # Flag to track if a greater element is found
    for j in range(
        nums2.index(nums1[i]) + 1, len(nums2)
    ):  # Start searching in nums2 after the current element's position
        if nums2[j] > nums1[i]:  # Check if a greater element is found
            res.append(nums2[j])  # Append the next greater element
            found = True  # Set the flag to true
            break  # Break out of the loop once found
    if not found:  # If no greater element is found
        res.append(-1)  # Append -1 to the result

# Print the result list
print("Next greater elements for nums1 in nums2:", res)
