# 189. Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Key is to use a temporary variable to hold the last element of the array
# and then to shift the elements of the array to the right by one position
# and then to assign the last element to the first position.
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]