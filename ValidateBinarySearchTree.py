# https://leetcode.com/problems/validate-binary-search-tree/
# Recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def smallestValue(self, root):
        if root.left is None and root.right is None:
            return root.val
        elif root.left is None:
            return min(root.val, self.smallestValue(root.right))
        elif root.right is None:
            return min(self.smallestValue(root.left), root.val)
        else:
            return min(root.val, min(self.smallestValue(root.left), self.smallestValue(root.right)))

    def largestValue(self, root):
        if root.left is None and root.right is None:
            return root.val
        elif root.left is None:
            return max(root.val, self.largestValue(root.right))
        elif root.right is None:
            return max(self.largestValue(root.left), root.val)
        else:
            return max(root.val, max(self.largestValue(root.left), self.largestValue(root.right)))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left:
            small = self.largestValue(root.left)
            if small >= root.val:
                return False
        
        if root.right:
            large = self.smallestValue(root.right)
            if large <= root.val:
                return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)