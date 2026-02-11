# 796. Rotate String
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

# Key is to use a sliding window to check if the string can be rotated to the goal string.
# If the string can be rotated to the goal string, return True.
# Otherwise, return False.

# example:
# Input: s = "abcde", goal = "cdeab"
# Output: true

# example:
# Input: s = "abcde", goal = "abced"
# Output: false

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if s == goal:
            return True
            
        for i in range(len(s) - 1):
            s = s[1:] + s[:1]
            if s == goal:
                return True

        return False

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        return goal in s + s