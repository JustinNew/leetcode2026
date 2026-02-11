# 18. 4Sum
# https://leetcode.com/problems/4sum/
# Key is to sort the nums first, then reduce it to 2Sum by moving beginning and end
# Then, use two pointers to find the two numbers that sum to the target value.
# Sort the array first to avoid duplicates.
# Very similar to 3Sum problem, only do the first repeated number once.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

# o(n^3) time complexity, o(1) space complexity
# Key is to sort the nums first, then reduce it to 2Sum by moving beginning and end
# Then, use two pointers to find the two numbers that sum to the target value.
# Sort the array first to avoid duplicates.
# Very similar to 3Sum problem, only do the first repeated number once.

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the nums first, then reduce it to 2Sum by moving beginning and end
        nums = sorted(nums)

        n = len(nums)
        if n < 4:
            return []

        result = []
        for i in range(n - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            else:
                for j in range(i + 1, n - 2):
                    if j != i + 1 and nums[j] == nums[j - 1]:
                        continue
                    s = target - nums[i]- nums[j]
                    l = j + 1
                    r = n - 1
                    while l < r:
                        if nums[l] + nums[r] == s:
                            result.append([nums[i], nums[j], nums[l], nums[r]])
                            while l < r and nums[l + 1] == nums[l]:
                                l += 1
                            l += 1
                        elif nums[l] + nums[r] > s:
                            r -= 1
                        else:
                            l += 1

        return result