# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Key is to use two pointers to find the two numbers that sum to the target value.
# Sort the array first to avoid duplicates.
# Very similar to 3Sum problem, only do the first repeated number once.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0

# Same as 3Sum
# Sort array first
# Skip the first repeated number
# Then, use two pointers
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        result = float('inf')
        for i in range(len(nums) - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(result - target):
                    result = total

                if total >= target:
                    k -= 1
                elif total < target:
                    j += 1
        
        return result