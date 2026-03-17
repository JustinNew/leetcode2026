# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
# Key is to use a linear scan and count the number of consecutive ones.
# Reset the count when encounter 0.

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # linear scan and count
        # reset when encounter 0
        result = 0
        count = 0
        for n in nums:
            if n == 0:
                result = max(result, count)
                count = 0
            else:
                count += 1

        result = max(result, count)
        
        return result
        