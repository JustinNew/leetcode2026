# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
# Key is to use a DFS to find all the paths that sum to the target sum.
# We can use a helper function to find all the paths that sum to the target sum.
# We can use a recursive function to find all the paths that sum to the target sum.
# Finally, return the result.

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# DP solution
# For patterns like a*, .*, or b*, * matches zero or more of the preceding element:
#   Zero Occurrence: 
#       dp[i][j] = dp[i][j-2] (skip * and its preceding element).
#   One or More Occurrences: 
#       dp[i][j] = dp[i-1][j] if s[i-1] matches p[j-2].
# For patterns like a, b, or c, they match themselves:
#   dp[i][j] = dp[i-1][j-1] if s[i-1] matches p[j-1].

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return dp[m][n]