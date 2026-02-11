# 102. Binary Tree Level Order Traversal
# Key is to have a temp list to store the next level nodes and a levels list to store the current level vals

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        q = []

        q.append(root)
        while q:
            levels = []
            temp = []

            for n in q:
                levels.append(n.val)
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)

            res.append(levels)
            q = temp

        return res 