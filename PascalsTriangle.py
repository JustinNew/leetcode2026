# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# Key is to use a nested loop to generate the triangle.
# The first and last element of each row is 1.
# The other elements are the sum of the two elements above it.

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

# o(n^2) time complexity, o(n^2) space complexity
# Key is to use a nested loop to generate the triangle.
# The first and last element of each row is 1.
# The other elements are the sum of the two elements above it.
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        result = [[1]]
        for i in range(1, numRows):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[-1][j - 1] + result[-1][j])

            result.append(temp)

        return result