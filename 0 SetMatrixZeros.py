# https://leetcode.com/problems/set-matrix-zeroes/
# Key is to use two lists to store the rows and columns that need to be set to zero
# and then to iterate through the matrix and set the rows and columns to zero
# and to return the modified matrix

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)

        for i in range(m):
            for j in range(n):
                if (i in rows or j in cols) and matrix[i][j] != 0:
                    matrix[i][j] = 0

        return

# Solution 2: Using inf to mark the rows and columns that need to be set to zero
# and then to iterate through the matrix and set the rows and columns to zero
# and to return the modified matrix
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for col in range(n):
                        if col != j and matrix[i][col] != 0:
                            matrix[i][col] = float('inf')
                    for row in range(m):
                        if row != i and matrix[row][j] !=0:
                            matrix[row][j] = float('inf')

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0

        return
    
# Solution 3: Using the first row and column as a note
# and then to iterate through the matrix and set the rows and columns to zero
# and to return the modified matrix
# Key is we first need to check if the first row and column contains zero and use two flags to mark it 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = False        
        first_col_has_zero = False

        # check if the first row contains zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # check if the first column contains zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        
        # use the first row and column as a note
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # set the marked rows to zero
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        # set the marked columns to zero
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
    
        # set the first row to zero if needed
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # set the first column to zero if needed
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
        
        return matrix

# Solution 4: Using the first row and column as a note
# and then to iterate through the matrix and set the rows and columns to zero
# and to return the modified matrix
# Key is we first need to check if the first row and column contains zero and use two flags to mark it 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = False
        column_flag = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                column_flag = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                row_flag = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_flag:
            for j in range(n):
                matrix[0][j] = 0
        if column_flag:
            for i in range(m):
                matrix[i][0] = 0

        return 