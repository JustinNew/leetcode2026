# 198. House Robber
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Use DP
# dp_y[i] = max(dp_y[i - 1], dp_y[i - 2] + nums[i])
# dp_n[i] = max(dp_n[i - 1], dp_n[i - 2] + nums[i])
# return max(dp_y[-1], dp_n[-1])
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP
        n = len(nums)
        if n <= 1:
            return nums[0]

        dp_y = [0 for i in range(n)]
        dp_n = [0 for i in range(n)]

        for i in range(n):
            if i == 0:
                dp_y[i] = nums[i]
                dp_n[i] = 0
            elif i == 1:
                dp_y[i] = nums[i]
                dp_n[i] = nums[0]
            else:
                dp_y[i] = nums[i] + max(max(dp_n[i - 1], dp_n[i - 2]), dp_y[i - 2])
                dp_n[i] = max(max(max(dp_y[i - 1], dp_n[i - 1]), dp_y[i - 2]), dp_n[i - 2])

        return max(dp_y[-1], dp_n[-1])

# Better solution
# At each house, we can either rob it or not rob it.
# Rob, max = nums[i] + dp[i-2]
# Not rob, max = dp[i-1]
# dp[i] = max(rob, not rob)
# return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1] 