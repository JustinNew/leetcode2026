# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Bit manipulation
# Key is to use bit manipulation to find the single number.
# We can use a XOR operation to find the single number.
# XOR operation is a binary operation that returns 1 if the bits are different, otherwise 0.
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result = result ^ n

        return result