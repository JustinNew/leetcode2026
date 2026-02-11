# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

from typing import List

# Key is to use a hash map to store the frequency of each element in the array.
# Then, return the element with the highest frequency.
# o(N) time complexity, o(N) space complexity
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        l = len(nums)
        for i in nums:
            d[i] += 1
        
        for i in d:
            if d[i] > l // 2:
                return i

# o(N) time complexity, o(1) space complexity
# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       res = majority = 0
        
       for n in nums:
           if majority == 0:
               res = n
        
           majority += 1 if n == res else -1
    
       return res