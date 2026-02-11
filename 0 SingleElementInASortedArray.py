# https://leetcode.com/problems/single-element-in-a-sorted-array/
# 540. Single Element in a Sorted Array
# Using binary search to find the single element in a sorted array
# Find the middle point
# Check if the middle point is the single element
# If not, check if the single element is on the left or right of the middle point
# If the single element is on the left, update the right pointer to the middle point - 2
# If the single element is on the right, update the left pointer to the middle point + 2
# If the single element is found, return the middle point
# If the single element is not found, return the left pointer

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            print(left, mid, right)
            val_m = nums[mid]
            if mid - 1 >= 0:
                val_left = nums[mid - 1]
            else:
                val_left = None

            if mid + 1 <= len(nums) - 1:
                val_right = nums[mid + 1]
            else:
                val_right = None

            if val_left == val_m:
                if (mid + 1) % 2 == 0:
                    left = mid + 1
                else: 
                    right = mid - 2
            
            elif val_right == val_m:
                if (len(nums) - mid) % 2 == 0:
                    right = mid - 1
                else:
                    left = mid + 2

            else:
                return nums[mid]

        return nums[left]