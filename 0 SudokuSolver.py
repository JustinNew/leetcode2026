# 37. Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:

# Backtracking solution
# Try, recurse, undo (backtrack)

from typing import List
class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # initialize
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    v = board[r][c]
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[(r // 3) * 3 + (c // 3)].add(v)

        def dfs(r, c):
            if r == 9:
                return True
            if c == 9:
                return dfs(r + 1, 0)
            if board[r][c] != '.':
                return dfs(r, c + 1)

            b = (r // 3) * 3 + (c // 3)

            for v in '123456789':
                if v not in rows[r] and v not in cols[c] and v not in boxes[b]:
                    board[r][c] = v
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[b].add(v)

                    if dfs(r, c + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(v)
                    cols[c].remove(v)
                    boxes[b].remove(v)

            return False

        dfs(0, 0)

# My solution
# It gets Time Limit Exceeded
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, s):
            # Check row
            for i in range(9):
                if board[row][i] == s:
                    return False

            # Check col
            for i in range(9):
                if board[i][col] == s:
                    return False

            # Check cell
            cell_r = row // 3 
            cell_c = col // 3
            for i in range(3):
                for j in range(3):
                    r = i + cell_r * 3
                    c = j + cell_c * 3
                    if board[r][c] == s:
                        return False

            return True

        def dfs(row, col):
            if row == 9:
                return True

            if col == 9:
                return dfs(row + 1, 0)

            if board[row][col] == '.':
                for i in range(1, 10):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)

                        if dfs(row, col + 1):
                            return True
                        else:
                            board[row][col] = '.'
                return False
            else:
                return dfs(row, col + 1)

            return

        dfs(0, 0)
