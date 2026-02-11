# https://leetcode.com/problems/spiral-matrix-ii/
# Key is to use the same logic as the SpiralMatrixI problem
# Use four boundaries to control the matrix
# 59. Spiral Matrix II

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        results = [[0 for i in range(n)] for j in range(n)]
        count = 0
        col_start = 0
        col_end = n - 1
        row_start = 0
        row_end = n - 1

        while count < n * n:
            for col in range(col_start, col_end + 1):
                count += 1
                results[row_start][col] = count

            row_start += 1

            for row in range(row_start, row_end + 1):
                count += 1
                results[row][col_end] = count

            col_end -= 1

            for col in range(col_end, col_start - 1, -1):
                count += 1
                results[row_end][col] = count

            row_end -= 1

            for row in range(row_end, row_start - 1, -1):
                count += 1
                results[row][col_start] = count

            col_start += 1

        return results