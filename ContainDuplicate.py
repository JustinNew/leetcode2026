# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Hash table
# Scan once
# If the number is already in the dict, return True
# If the number is not in the dict, add it to the dict
# Return False

from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a dict
        # Scan once
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
            if d[n] > 1:
                return True

        return False

# Use a set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False