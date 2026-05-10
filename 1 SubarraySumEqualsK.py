# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Explanation: The subarrays [1,1] and [1,1] are the
# only subarrays that sum to 2.
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# Explanation: The subarrays [1,2] and [3] are the only sub
# arrays that sum to 3.

# We need to find two types of subarrays: 
# one that starts at index 0 and 
# another that starts somewhere in the middle of the array.
# In other words, the number of subarrays with a total equal to total - k
# corresponds to the number of subarrays that sum up to k (=7).
# This algorithm needs to have total of subarray and frequency of the total.
# One important is that we initialize the HashMap with {0:1}.

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0:1}
        total = count = 0

        for n in nums:
            total += n
            
            if total - k in sub_num:
                count += sub_num[total-k]
            
            sub_num[total] = 1 + sub_num.get(total, 0)
        
        return count