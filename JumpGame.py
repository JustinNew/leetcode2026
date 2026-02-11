# 55. Jump Game
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