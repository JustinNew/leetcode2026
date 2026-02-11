# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            checked = 1
            current = 1
            while checked < len(nums):
                if nums[checked] != nums[current - 1]:
                    nums[current] = nums[checked]
                    current += 1
                checked += 1

            return current