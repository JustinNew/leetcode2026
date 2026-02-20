# 216. Combination Sum III
# Given an integer k, return all possible combinations of k numbers chosen from the range [1, 9].
# You may return the answer in any order.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9

# DFS
from typing import List
class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        arr = [i for i in range(1, 10)]

        result = []
        def dfs(nums, target, comb):
            if target == 0 and len(comb) == k:
                result.append(comb)
                return
            if target < 0:
                return 
            
            for i in range(len(nums)):
                if nums[i] <= target:
                    dfs(nums[i + 1:], target - nums[i], comb + [nums[i]])

            return

        dfs(arr, target, [])
        return result