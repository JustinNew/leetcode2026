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

# 20260308 Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP

        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = True

        result = s[0]
        for i in range(1, n):
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > len(result):
                        result = s[j:i + 1]

        return result

# 20260504 Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Use DP
        # dp[begin][end] = True
        l = len(s)

        if l <= 1:
            return s

        result = s[0]

        dp = [[False for i in range(l)] for j in range(l)]
        for i in range(l):
            dp[i][i] = True

        for end in range(1, l):
            for begin in range(end):
                if s[begin] == s[end]:
                    if end - begin <= 2:
                        dp[begin][end] = True
                        if len(result) < end - begin + 1:
                            result = s[begin:end + 1]
                    elif dp[begin + 1][end - 1] == True:
                        dp[begin][end] = True
                        if len(result) < end - begin + 1:
                            result = s[begin:end + 1]

        return result