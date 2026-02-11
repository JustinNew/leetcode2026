# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Key is to use DFS to traverse the grid and count the number of islands.
# We use a visited matrix to track the visited nodes.
# We use a land matrix to track the land nodes.
# We use a dfs function to traverse the grid and count the number of islands.

from typing import List

# This is using BFS to traverse the grid and count the number of islands.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])

        visited = [[False for i in range(num_col)] for j in range(num_row)]
        island = 0

        for i in range(num_row):
            for j in range(num_col):
                if visited[i][j] == False:
                    if grid[i][j] == "1":
                        island += 1
                        land = []
                        land.append((i, j))
                        while land:
                            temp = []
                            for (k, l) in land:
                                if k + 1 < num_row and not visited[k + 1][l] and grid[k + 1][l] == "1":
                                    temp.append((k + 1, l))
                                    visited[k + 1][l] = True
                                if l + 1 < num_col and not visited[k][l + 1] and grid[k][l + 1] == "1":
                                    temp.append((k, l + 1))
                                    visited[k][l + 1] = True
                                if k - 1 >= 0 and not visited[k - 1][l] and grid[k - 1][l] == "1":
                                    temp.append((k - 1, l))
                                    visited[k - 1][l] = True
                                if l - 1 >= 0 and not visited[k][l - 1] and grid[k][l - 1] == "1":
                                    temp.append((k, l - 1))
                                    visited[k][l - 1] = True
                            land = temp
                visited[i][j] = True

        return island

# Optimized solution using DFS and a flag to track the visited nodes.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.result = 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.flag = [['unseen' for i in range(self.n)] for j in range(self.m)]

        def dfs(grid, i, j):
            if i < 0 or i >= self.m or j < 0 or j >= self.n:
                return
            elif grid[i][j] == "0":
                return

            if self.flag[i][j] == 'visited' or self.flag[i][j] == 'visiting':
                return
            elif self.flag[i][j] == 'unseen':
                self.flag[i][j] = 'visiting'
                dfs(grid, i - 1, j)
                dfs(grid, i + 1, j)
                dfs(grid, i, j - 1)
                dfs(grid, i, j + 1)
                self.flag[i][j] = 'visited'
                return

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1" and self.flag[i][j] == 'unseen':
                    self.result += 1
                    dfs(grid, i, j)

        return self.result