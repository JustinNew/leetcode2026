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

# 20260511 Solution
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # From left to right
        # Find the first decreasing number
        # Exchange with the smallest number that is larger than that number
        # Sort the rest

        l = len(nums)
        pivot = -1
        for i in range(l - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            nums.sort()
            return

        change = pivot + 1
        for i in range(pivot + 2, l):
            if nums[i] > nums[pivot] and nums[change] > nums[i]:
                change = i

        nums[pivot], nums[change] = nums[change], nums[pivot]

        nums[pivot + 1:] = sorted(nums[pivot + 1:])

        return