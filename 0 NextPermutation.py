# 31. Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the next permutation of arr is [1,3,2].
# Similarly, the next permutation of arr = [3,2,1] is [1,2,3].
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.

# Key is to find the pivot point and then find the successor and then reverse the suffix.

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 1. find pivot
        i = -1
        for k in range(n - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                i = k
                break

        if i == -1:
            nums.reverse()
            return

        # 2. find successor
        for j in range(n - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break

        # 3. reverse suffix
        nums[i + 1:] = reversed(nums[i + 1:])

        return