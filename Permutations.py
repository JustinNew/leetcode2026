# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

# Key is to use a DFS to generate all possible permutations.
# We can use a helper function to generate all possible permutations.
# We can use a recursive function to generate all possible permutations.

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(arr, comb):
            if len(arr) == 0:
                result.append(comb)
                return

            for i in range(len(arr)):
                dfs(arr[:i] + arr[i+1:], comb + [arr[i]])

            return

        dfs(nums, [])

        return result

# 20260305 Solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # DFS
        # Each step, choose one from the remaining numbers

        result = []
        def dfs(arr, comb):
            if len(arr) == 0:
                result.append(comb)
                return

            for i in range(len(arr)):
                dfs(arr[:i] + arr[i+1:], comb + [arr[i]])

            return

        dfs(nums, [])

        return result 