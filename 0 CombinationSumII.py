from typing import List

# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
# Key is to use a recursive approach to generate all possible combinations.
# We can use a hash set to store the combinations.
# We can use a hash set to store the combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: [[1,2,2],[5]]

# Key is to use a recursive approach to generate all possible combinations.
# We can use a hash set to store the combinations.
# We can use a hash set to store the combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        groups = [[]]
        candidates = sorted(candidates)
        for n in candidates:
            if n <= target:
                temp = []
                for g in groups:
                    if sum(g + [n]) == target and g + [n] not in result:
                        result.append(g + [n])
                    elif sum(g + [n]) < target:
                        if g not in temp:
                            temp.append(g)
                        if g + [n] not in temp:
                            temp.append(g + [n])
                groups = temp

        return result