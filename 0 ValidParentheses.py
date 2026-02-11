# 32. Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0

# Key is to use dynamic programming to find the longest valid parentheses substring.
# Use a dp array to store the length of the longest valid parentheses substring ending at index i.

from typing import List

# DP solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':  # "()" pattern
                    dp[i] = 2 + (dp[i - 2] if i >= 2 else 0)
                else:
                    prev = i - dp[i - 1] - 1
                    if prev >= 0 and s[prev] == '(':
                        dp[i] = dp[i - 1] + 2
                        if prev >= 1:
                            dp[i] += dp[prev - 1]
                max_len = max(max_len, dp[i])

        return max_len

# Two pass solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left =0
        right =0
        maxlen = 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2 * right)
            elif right > left:
                left = right = 0

        left=right=0
        for ch in reversed(s):
            if ch==")":
                right +=1
            else:
                left+=1
            if right==left:
                maxlen=max(maxlen,2*left)
            elif left>right:
                left=right=0
            

        return maxlen
