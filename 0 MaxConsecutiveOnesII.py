# 487. Max Consecutive Ones II
# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

# Example 1:
# Input: nums = [1,0,1,0,1]
# Output: 4
# Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

# Example 2:
# Input: nums = [1,0,1,0,1,0,1]
# Output: 4
# Explanation: Flip the second zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # DP
        # dp[i][j] from i to j, how many 0s are there.

        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(n)]

        result = 0
        for i in range(n):
            if nums[i] == 0:
                dp[i][i] = 1

            for j in range(i):
                if nums[i] == 0:
                    dp[j][i] = dp[j][i - 1] + 1
                else:
                    dp[j][i] = dp[j][i - 1]
                
                if dp[j][i] <= k and i - j + 1 > result:
                    result = i - j + 1

        return result