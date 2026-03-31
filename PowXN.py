# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Key is to use a while loop to calculate the power of x.
# We can use a flag to mark if the result is negative.
# We can then use a while loop to calculate the power of x.
# We can then use a if statement to check if the result is greater than the maximum value of 32-bit integer.
# If it is, we return the maximum value of 32-bit integer.
# Otherwise, we return the result.

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000

# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

# TLE: Time Limit Exceeded
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        flag = False
        if n < 0:
            flag = True
            n = -1 * n

        result = 1
        while n > 0:
            result = result * x
            n -= 1

        if flag:
            result = 1 / result

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < -1 * 2 ** 31:
            return -1 * 2 ** 31
        else:
            return result

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc_pow(x, n):

            if n == 0:
                return 1
            res = calc_pow(x, n // 2)

            if n % 2 == 0:
                return res * res
            else:
                return res * res * x
        
        if n < 0:
            return 1 / calc_pow(x, -1 * n)

        return calc_pow(x, n)