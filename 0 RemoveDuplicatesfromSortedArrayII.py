# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3]

# Use two pointers approach.
# Not so easy to be bug free.
# ndx keeps track of checking elements.
# current keeps track of assigned elements.
# Check nums[ndx] != nums[current - 1] or nums[ndx] != nums[current - 2] to avoid duplicates.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two pointers approach
        # One pointer move forward
        # One pointer keep track of assigned elements
        n = len(nums)
        if n <= 2:
            return n

        ndx = 2
        current = 2
        for ndx in range(2, n):
            if nums[ndx] != nums[current - 1] or nums[ndx] != nums[current - 2]:
                nums[current] = nums[ndx]
                current += 1

        return current