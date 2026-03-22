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

# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,0,1,0,1], k = 2
# Output: 4
# Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

# Example 2:
# Input: nums = [1,0,1,0,1,0,1], k = 2
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

# Sliding window approach
# Update the result for every front trigger
# Update the back pointer when zero_count > k
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding window approach
        # Two pointers
        # When front triggered count of 0 = k, do calculation, and move back forward
        back = 0
        zero_count = 0
        result = 0

        for front in range(len(nums)):
            if nums[front] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[back] == 0:
                    zero_count -= 1
                back += 1

            result = max(result, front - back + 1)

        return result