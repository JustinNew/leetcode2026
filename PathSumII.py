# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/
# Key is to use a DFS to find all the paths that sum to the target sum.
# We can use a helper function to find all the paths that sum to the target sum.
# We can use a recursive function to find all the paths that sum to the target sum.
# Finally, return the result.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths that sum to 22: 5 + 4 + 11 + 2 = 22 and 5 + 8 + 4 + 5 = 22.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: []

# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: []

# DFS
# Memorize the Suffix solutions
from typing import List, Optional
from typing import TreeNode
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []

        def dfs(root, comb):
            if not root.left and not root.right:
                if sum(comb) + root.val == targetSum:
                    result.append(comb + [root.val])
                return

            if root.left:
                dfs(root.left, comb + [root.val])
            if root.right:
                dfs(root.right, comb + [root.val])

            return

        if not root:
            return []

        dfs(root, [])
        return result