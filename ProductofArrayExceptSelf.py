# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Two-pass algorithm
# One to get multiply from left so far
# One to get multiply from right so far
# Last run to get the result
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_run = [1 for i in range(n)]
        right_run = [1 for i in range(n)]

        result = 1
        for i in range(n - 1):
            result = result * nums[i]
            left_run[i] = result

        result = 1
        for i in range(n - 1, 0, -1):
            result = result * nums[i]
            right_run[i] = result

        result = []
        for i in range(n):
            if i == 0:
                result.append(right_run[i + 1])
            elif i == n - 1:
                result.append(left_run[i - 1])
            else:
                result.append(left_run[i - 1] * right_run[i + 1])

        return result