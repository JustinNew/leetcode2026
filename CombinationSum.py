# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# Key is to use a DFS to find all unique combinations of candidates where the chosen numbers sum to target.
# Same number can be used again and again. So, need to pass the current index to the DFS function.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Use a DFS
        candidates = sorted(candidates)

        result = []

        def dfs(t, nums, comb):
            if t < 0:
                return
            
            if t == 0:
                result.append(comb)
                return 
            
            for i in range(len(nums)):
                dfs(t - nums[i], nums[i:], comb + [nums[i]])

            return

        dfs(target, candidates, [])

        return result