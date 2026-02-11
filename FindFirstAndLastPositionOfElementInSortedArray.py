# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 34. Find First and Last Position of Element in Sorted Array

from typing import List

class Solution:
    def findLeftIndex(self, nums, target):
        if len(nums) == 0:
            return -1

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid - 1 >= 0 and nums[mid - 1] < target:
                    return mid
                elif mid == 0:
                    return mid
                else:
                    right = mid - 1

        return -1

    def findRightIndex(self, nums, target):
        if len(nums) == 0:
            return -1

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid + 1 <= len(nums) - 1 and nums[mid + 1] > target:
                    return mid
                elif mid == len(nums) - 1:
                    return mid
                else:
                    left = mid + 1

        return -1    

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.findLeftIndex(nums, target)
        right_index = self.findRightIndex(nums, target)

        return [left_index, right_index]