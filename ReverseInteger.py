# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Key is to handle the edge cases and to return the correct result.
# We can use a flag to mark if the number is negative and then convert the number to positive.
# We can then use a while loop to reverse the number.
# We can then use a if statement to check if the result is greater than the maximum value of 32-bit integer.
# If it is, we return 0.
# Otherwise, we return the result.

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Example 4:
# Input: x = 0
# Output: 0

# o(log(x)) time complexity, o(1) space complexity
# Key is to handle the edge cases and to return the correct result.
# We can use a flag to mark if the number is negative and then convert the number to positive.
# We can then use a while loop to reverse the number.
# We can then use a if statement to check if the result is greater than the maximum value of 32-bit integer.
# If it is, we return 0.
# Otherwise, we return the result.
class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = -1 * x

        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10

        if flag:
            if result > 2 ** 31:
                return 0
            else:
                return -1 * result
        else:
            if result > 2 ** 31 - 1:
                return 0
            else:
                return result