# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Key is to have 4 pointers to track the boundaries of the matrix
# and then to iterate through the matrix in a spiral order
# and to add the elements to the results list
# and to update the boundaries of the matrix
# and to break the loop when the count is equal to the number of elements in the matrix
# and to return the results list

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count = 0
        m = len(matrix)
        n = len(matrix[0])

        first_row = 0
        last_row = m - 1
        first_column = 0 
        last_column = n - 1
        results = []

        while True:
            # Right
            for i in range(first_column, last_column + 1):
                results.append(matrix[first_row][i])
                count += 1
            first_row += 1
            if count == m * n:
                break

            # Down
            for j in range(first_row, last_row + 1):
                results.append(matrix[j][last_column])
                count += 1
            last_column -= 1
            if count == m * n:
                break

            # Left
            for i in range(last_column, first_column - 1, -1):
                results.append(matrix[last_row][i])
                count += 1
            last_row -= 1
            if count == m * n:
                break

            # Up
            for j in range(last_row, first_row - 1, -1):
                results.append(matrix[j][first_column])
                count += 1
            first_column += 1
            if count == m * n:
                break
        
        return results

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0 
        right = n - 1
        result = []
        count = 0
        while top <= bottom:
            # to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
                count += 1
            top += 1

            if count >= m * n:
                break

            # to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
                count += 1
            right -= 1

            if count >= m * n:
                break 

            # to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
                count += 1
            bottom -= 1

            if count >= m * n:
                break

            # to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
                count += 1
            left += 1

            if count >= m * n:
                break
        
        return result