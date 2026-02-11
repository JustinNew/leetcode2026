# 44. Wildcard Matching
# Given an input string (s) and a pattern (p), implement wildcard matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

# Time out solution
# Not optimized
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        s = '~' + s
        p = '~' + p

        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n+ 1):
            if p[j] == '*':
                for i in range(m + 1):
                    if j == 1:
                        dp[i][j] = True
                    else:
                        for l in range(i + 1):
                            if dp[l][j - 1] == True:
                                dp[i][j] = True
            elif p[j] == '?':
                for i in range(m + 1):
                    if i != 0 and dp[i - 1][j - 1] == True:
                        dp[i][j] = True
            else:
                for i in range(m + 1):
                    if i != 0 and dp[i - 1][j - 1] == True and p[j] == s[i]:
                        dp[i][j] = True

        return dp[m][n]

# Optimized solution
# The key is for the * case, it can be empty, one, or more characters. 
# So we need to check if the * can be empty, one, or more characters. 
# If it can be empty, we need to check if the previous character is matched. 
# If it can be one character, we need to check if the previous character is matched. 
# If it can be more characters, we need to check if the previous character is matched. 
# Once we find a match, we can set the matched flag to True and set the rest of the rows in the same column to True. 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        s = '~' + s
        p = '~' + p

        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            matched = False
            for i in range(m + 1):
                if p[j] == '*':
                    if matched == True:
                        dp[i][j] = True
                    elif dp[i][j - 1] == True:
                        dp[i][j] = True
                        matched = True
                    elif i > 0 and dp[i - 1][j - 1] == True:
                        dp[i][j] = True
                        matched = True
                elif p[j] == '?' and i > 0 and dp[i - 1][j - 1] == True:
                    dp[i][j] = True
                elif p[j] == s[i] and i > 0 and dp[i - 1][j - 1] == True:
                    dp[i][j] = True

        return dp[m][n]