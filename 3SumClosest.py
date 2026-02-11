# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Key is to use two pointers to find the two numbers that sum to the target value.
# Sort the array first to avoid duplicates.
# Very similar to 3Sum problem, only do the first repeated number once.
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