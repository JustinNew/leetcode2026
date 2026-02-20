# 220. Contains Duplicate III
# Given an integer array nums and two integers indexDiff and valueDiff, return true if there are two distinct indices i and j in the array such that abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff.

# Example 1:
# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true

# Example 2:
# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false

# Sliding window
# Scan once and compare
# Use a deque to store the indices of the numbers
# If the difference between the current index and the index of the number is less than or equal to indexDiff, return True
# If the difference between the current index and the index of the number is greater than indexDiff, remove the number from the deque
# Return False

# This solution has Time Limit Exceeded issue.
from typing import List
from collections import deque
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Use a deque
        # Scan once and compare
        dq = deque()

        def withinDiff(val, arr):
            for n in arr:
                if abs(val - n) <= valueDiff:
                    return True
            
            return False

        for i in range(len(nums)):
            if withinDiff(nums[i], dq):
                return True

            if len(dq) >= indexDiff:
                dq.popleft()
            dq.append(nums[i])

        return False

# Use bucket
# We can summarize numbers in a given range into bucket.
# Then, we can check if the number is in the same bucket or the adjacent buckets.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False # edge case 
        
        seen = {}
        for i, x in enumerate(nums): 
            bkt = x//(t+1)
            if bkt in seen and i - seen[bkt][0] <= k: return True 
            if bkt-1 in seen and i - seen[bkt-1][0] <= k and abs(x - seen[bkt-1][1]) <= t: return True 
            if bkt+1 in seen and i - seen[bkt+1][0] <= k and abs(x - seen[bkt+1][1]) <= t: return True 
            seen[bkt] = (i, x) 
        return False 