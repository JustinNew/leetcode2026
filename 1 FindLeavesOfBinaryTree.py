# 366. Find Leaves of Binary Tree
# Given a binary tree, collect a tree's nodes as if you were doing this: 
# Collect and remove all leaves, repeat until the tree is empty.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Definition for a binary tree node.
# DFS solution
# Post-order traversal
# Calculate the height
# Height of root = 1 + max(height of left subtree, height of right subtree)
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node):
            if not node:
                return -1

            left_h = dfs(node.left)
            right_h = dfs(node.right)

            h = max(left_h, right_h) + 1

            if h == len(result):
                result.append([])

            result[h].append(node.val)
            return h

        dfs(root)
        return result