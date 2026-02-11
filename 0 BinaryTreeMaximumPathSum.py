# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# 124. Binary Tree Maximum Path Sum
# Key is to have a variable to keep track of Max
# There are two ways to get max: 
# 1. max is root + left + right; 
# 2. max needs to go upper with either root + left or root + right. 
# Also, left or right should not be less than 0. 

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = float('-inf')

        def dfs(root):
            if not root: 
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            self.res = max(self.res, root.val + left + right)
        
            return root.val + max(left, right)

        dfs(root)

        return self.res