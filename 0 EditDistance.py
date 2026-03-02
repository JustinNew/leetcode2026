# 72. Edit Distance
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')

# Example 3:
# Input: word1 = "", word2 = ""
# Output: 0

# Example 4:
# Input: word1 = "a", word2 = "b"
# Output: 1
# Explanation: 
# a -> b (replace 'a' with 'b')

# Example 5:
# Input: word1 = "ab", word2 = "ac"
# Output: 1
# Explanation: 
# ab -> ac (replace 'b' with 'c')

# Key is to use dynamic programming to find the minimum number of operations to convert word1 to word2
# DP solution with memoization
# dp(i, j) = minimum number of operations needed to convert
#          the first i characters of word1
#          to the first j characters of word2
# Insert: dp(i, j) = 1 + dp(i, j-1)
# Delete: dp(i, j) = 1 + dp(i - 1, j)
# Replace: dp(i, j) = dp(i-1, j-1)
# Equal: dp(i, j) = dp(i-1, j-1)
# Very tricky

'''
edit("horse", "ros")
├── delete → edit("orse", "ros")
│   └── replace → edit("rse", "os")
│       └── ...
├── insert → edit("horse", "os")
│   └── delete → edit("orse", "os")
│       └── ...
├── replace → edit("orse", "os")
    └── ...
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i == 0:
                return j
            if j == 0:
                return i

            if word1[i - 1] == word2[j - 1]:
                res = dp(i - 1, j - 1)
            else:
                res = 1 + min(
                    dp(i - 1, j),      # Delete
                    dp(i, j - 1),      # Insert
                    dp(i - 1, j - 1)   # Replace
                )

            cache[(i, j)] = res
            return res

        return dp(len(word1), len(word2))