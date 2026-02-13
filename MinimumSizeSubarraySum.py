# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Explanation: The subarray [4] has the minimal length under the problem constraint.

# Key is to use a sliding window to find the minimum size subarray sum.
# We can use a left pointer to store the left index of the subarray.
# We can use a right pointer to store the right index of the subarray.
# We can use a current sum to store the sum of the subarray.
# We can use a result to store the minimum size of the subarray.
# We can then use a while loop to find the minimum size subarray sum.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        result = 0
        current_sum = nums[0]
        while True:
            if current_sum >= target:
                if result != 0:
                    result = min(result, right - left + 1)
                else:
                    result = right - left + 1
                current_sum = current_sum - nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    current_sum = current_sum + nums[right]
                else:
                    break
                
        return result