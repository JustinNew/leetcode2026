# 33. Search in Rotated Sorted Array
# Given an integer array nums sorted in ascending order, and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# Key is to compare the middle point with the right point for the pivot point
# If the right does not contain pivot point, then the middle point must be smaller than the right point
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def findPivot(nums: List[int]) -> int:
            if len(nums) == 0:
                return None

            left = 0 
            right = len(nums) - 1

            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid

            return left

        def binarySearch(nums, target):
            if len(nums) == 0:
                return -1

            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1

        pivot = findPivot(nums)

        first = binarySearch(nums[0:pivot], target)
        second = binarySearch(nums[pivot:], target)

        if first == -1 and second == -1:
            return -1
        elif first != -1:
            return first
        else:
            return second + pivot