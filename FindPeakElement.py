# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if mid + 1 == len(nums) - 1 and nums[mid + 1] > nums[mid]:
                return mid + 1
            elif nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left

    class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)

        low = 0
        high = l - 1
        while low <= high:
            mid = (low + high) // 2
            if mid - 1 >= 0 and nums[mid] > nums[mid - 1] and mid + 1 < l and nums[mid] > nums[mid + 1]:
                return mid
            elif mid == 0:
                if mid + 1 < l and nums[mid] < nums[mid + 1]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] > nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1

        return mid