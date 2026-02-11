# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Binary Search
# Key is to find the row and column of the middle element.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m * n - 1

        while low <= high:
            med = low + (high - low) // 2
            row = med // n
            column  = med - row * n
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                low = med + 1
            else:
                high = med - 1

        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First do a binary search to find in which row 
        # Then do a binary seach in that row 

        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] > target or matrix[m - 1][n - 1] < target:
            return False

        # Search the row
        low = 0 
        high = m - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][n - 1] >= target:
                break
            else:
                low = mid + 1

        r = mid
        low = 0 
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False