# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# DFS
# + Memorization with backtracking

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS 
        # Need a table to memorize it is used or not

        m = len(board)
        n = len(board[0])

        l_word = len(word)

        def dfs(i, j, ndx):
            if ndx == l_word:
                return True

            if i + 1 < m and board[i + 1][j] == word[ndx] and not visited[i + 1][j]:
                visited[i + 1][j] = True
                if dfs(i + 1, j, ndx + 1):
                    return True
                visited[i + 1][j] = False

            if i - 1 >= 0 and board[i - 1][j] == word[ndx] and not visited[i - 1][j]:
                visited[i - 1][j] = True
                if dfs(i - 1, j, ndx + 1):
                    return True
                visited[i - 1][j] = False

            if j + 1 < n and board[i][j + 1] == word[ndx] and not visited[i][j + 1]:
                visited[i][j + 1] = True
                if dfs(i, j + 1, ndx + 1):
                    return True
                visited[i][j + 1] = False
            
            if j - 1 >= 0 and board[i][j - 1] == word[ndx] and not visited[i][j - 1]:
                visited[i][j - 1] = True
                if dfs(i, j - 1, ndx + 1):
                    return True
                visited[i][j - 1] = False

            return False
        
        visited = [[False for ni in range(n)] for mi in range(m)]
        for mi in range(m):
            for ni in range(n):
                if board[mi][ni] == word[0]:
                    visited[mi][ni] = True
                    if dfs(mi, ni, 1):
                        return True
                    visited[mi][ni] = False

        return False