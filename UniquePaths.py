# 62. Unique Paths
# Given two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner of the grid (starting from the top-left corner).

# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3

# Dynamic programming
# Use a m * n matrix to store the unique path 
# First row and first column are all 1
# Other cells are the sum of the cell above and the cell to the left
# Return the last cell of the matrix

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic programming
        result = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            result[i][0] = 1
        
        for j in range(n):
            result[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i - 1][j] + result[i][j - 1]

        return result[m - 1][n - 1]