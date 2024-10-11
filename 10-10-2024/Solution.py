# Code can be fun and creative! Just like how this matrix zigzags, sometimes the solution to a bug might also take a few zigzags before you get it right! 🚀😄

# Importing Numpy for matrix operations
import numpy as np


# Function to take input for a matrix from the user
def input_matrix():
    """
    Function to take matrix input from the user.
    Returns:
        mat (numpy.ndarray): Matrix with M rows and N columns as input by the user.
    """
    # Taking input for the number of rows and columns
    M = int(input("Enter Number of Rows: "))
    N = int(input("Enter Number of Columns: "))

    # Declaring a matrix of size MxN filled with zeros initially
    mat = np.zeros((M, N), dtype=int)

    # Loop to take input for each element of the matrix
    for i in range(M):
        for j in range(N):
            mat[i, j] = int(input(f"Enter Element for position [{i+1}, {j+1}]: "))

    return mat


# Predefined matrix for testing (3x3)
M, N = 3, 3
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Displaying the matrix
print("Matrix is:")
print(mat)


# Function to traverse the matrix in zigzag order
def zigzag_order_mat(mat, m, n):
    """
    Traverses the matrix in a zigzag pattern:
    - First and last rows are traversed left-to-right.
    - Middle rows are traversed right-to-left.

    Args:
        mat (numpy.ndarray): Matrix to be traversed.
        m (int): Number of rows.
        n (int): Number of columns.

    Returns:
        list: List containing matrix elements in zigzag order.
    """
    mat_trav_lst = []  # List to store the zigzag order

    for i in range(m):
        if i == 0 or i == m - 1:
            # Traverse left to right for the first and last row
            for j in range(n):
                mat_trav_lst.append(mat[i, j])
        else:
            # Traverse right to left for the middle rows
            for j in range(n - 1, -1, -1):
                mat_trav_lst.append(mat[i, j])

    return mat_trav_lst


# Displaying the zigzag order traversal
print("Zigzag Order Traversal Of Matrix is:")
print(zigzag_order_mat(mat, M, N))
