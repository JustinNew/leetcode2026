# 78. Subsets
# Given an integer array nums, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets.
# Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Key is to use a recursive approach to generate all possible subsets.
# We can use a helper function to generate all possible subsets.
# We can use a recursive function to generate all possible subsets.
# We can use a recursive function to generate all possible subsets.

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        result = [[]]
        for i in nums:
            temp = [p for p in result]
            new = []
            for j in temp:
                new.append(j + [i])
            result += new
        
        return result