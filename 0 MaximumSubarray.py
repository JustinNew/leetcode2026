# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# Key is to use a two pointers to find the contiguous subarray with the largest sum.
# We can use a current sum to store the sum of the contiguous subarray.
# If the current sum is less than 0, we can reset it to the current element.
# Otherwise, we can add the current element to the current sum.
# We can then update the result to the maximum of the current sum and the result.
# We can then return the result.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Use two pointers
        if len(nums) == 1:
            return nums[0]

        end = 1
        result = nums[0]
        current = nums[0]

        while end < len(nums):
            if current < 0:
                current = nums[end]
            else:
                current += nums[end] 

            result = max(current, result)

            end += 1

        return result