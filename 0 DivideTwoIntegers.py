# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
# Key is to use bit manipulation to divide the two integers.
# We can use a flag to mark if the result is negative.
# We can then use a while loop to divide the two integers.
# We can use a if statement to check if the result is greater than the maximum value of 32-bit integer.
# If it is, we return the maximum value of 32-bit integer.
# Otherwise, we return the result.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2

# Example 3:
# Input: dividend = 0, divisor = 1
# Output: 0

# Example 4:
# Input: dividend = 1, divisor = 1
# Output: 1

# Bit manipulation
# p << 1 is p * 2
# Every integer can be represented as a sum of powers of 2.
# 13 = 8 + 4 + 1 = 2³ + 2² + 2⁰
# 39 = 3 * 13 = 3 * (8 + 4 + 1) = 3 * 2³ + 3 * 2² + 3 * 2⁰
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            count = 0
            p = divisor
            while p << 1 < dividend:
                count += 1
                p = p << 1

            result += 1 << count
            dividend -= p

        if flag:
            return -1 * result
        else:
            if result >= 2 ** 31:
                return 2 ** 31 - 1
            else:
                return result