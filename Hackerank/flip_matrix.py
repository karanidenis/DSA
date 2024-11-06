#!usr/bin/python3

# flip matrix to find the maximum sum of the upper-left quadrant of the matrix
# The upper-left quadrant is the first n/2 rows and first m/2 columns of the matrix
def flip_matrix(matrix):
    n = len(matrix)
    max_sum = 0
    half_n = n // 2

    for i in range(half_n):
        for j in range(half_n):
            # Consider all possible flips for element matrix[i][j]
            top_left = matrix[i][j]
            top_right = matrix[i][n-1-j]
            bottom_left = matrix[n-1-i][j]
            bottom_right = matrix[n-1-i][n-1-j]
            
            # Take the maximum value among the possible flips
            max_sum += max(top_left, top_right, bottom_left, bottom_right)

    return max_sum

# Example usage
matrix = [
   [1, 2],[ 3, 4]
    # [5, 6, 7, 8],
    # [9, 10, 11, 12],
    # [13, 14, 15, 16]
]

print(flip_matrix(matrix))
