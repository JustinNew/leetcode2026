# 55. Jump Game
# https://leetcode.com/problems/jump-game/

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.

# Key is to have a variable to keep track of max reach. 
# If max reach is less than current index, return False. 
# If max reach is greater than or equal to current index, update max reach. 
# If max reach is greater than or equal to length of nums, return True. 

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i == 0:
                max_reach = nums[i]
            elif max_reach >= i:
                max_reach = max(max_reach, i + nums[i])
            elif max_reach < len(nums):
                return False

        return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        result = 0
        for i in range(len(nums)):
            if result < i:
                return False
            result = max(result, i + nums[i])

        return True