# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Key is to use dynamic programming to find the number of distinct ways to climb to the top.
# We can use a list to store the number of distinct ways to climb to the top for each step.
# We can use a for loop to iterate through the steps and update the list.
# We can return the last element of the list.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            result = [0 for i in range(n)]
            result[0] = 1
            result[1] = 2
            for i in range(2, n):
                result[i] = result[i - 1] + result[i - 2]

        return result[-1]