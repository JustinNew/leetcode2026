# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Key is to use dynamic programming to find the longest palindromic substring.
# We can use a 2D array to store the longest palindromic substring for each substring.
# We can then iterate through the string and update the 2D array.
# Finally, we can return the longest palindromic substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Use dynamic programming
        # dp[begin][end] = True

        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s

        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = True

        result = s[0]
        for i in range(1, n):
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1] == True):
                    dp[j][i] = True
                    if i - j + 1 > len(result):
                        result = s[j:i+1]

        return result