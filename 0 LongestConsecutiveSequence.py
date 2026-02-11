# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

from typing import List

# Key is to use a set to store the numbers in the array
# and then to iterate through the set and check if the current number is the start of a consecutive sequence
# if it is, then we can iterate through the set and check if the current number is in the set
# if it is, then we can increment the length of the consecutive sequence
# and then we can return the longest consecutive sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest