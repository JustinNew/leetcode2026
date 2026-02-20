# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Hash table
# Scan once
# If the number is already in the dict, check if the difference between the current index and the index of the number is less than or equal to k
# If it is, return True
# If it is not, update the index of the number in the dict
# Return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Use dict
        # Scan once
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and abs(i - d[nums[i]]) <= k:
                return True
            d[nums[i]] = i

        return False