# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# Key is to convert the strings to integers and then multiply them.
# Then, convert the result back to a string.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# o(m + n) time complexity, o(m + n) space complexity
# Key is to convert the strings to integers and then multiply them.
# Then, convert the result back to a string.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        t1 = 0
        t2 = 0
        for s in num1:
            t1 = t1 * 10 + ord(s) - ord('0')

        for s in num2:
            t2 = t2 * 10 + ord(s) - ord('0')

        return str(t1 * t2)