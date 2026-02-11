# 129. Sum Root to Leaf Numbers
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.

# Key is to use a preorder traversal to store the numbers in a list and then convert the list to a number.
# Then, add the number to the result.
# Finally, return the result.

# example:
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.result = 0 

        def dfs_preorder(root, nums):

            if not root.left and not root.right:
                s = 0
                temp = nums + [root.val]
                for i in range(len(temp)):
                    s = s * 10 + temp[i]
                self.result += s
            else:
                if root.left:
                    dfs_preorder(root.left, nums + [root.val])
                if root.right:
                    dfs_preorder(root.right, nums + [root.val])
            
        if not root:
            return 0

        dfs_preorder(root, [])
        return self.result

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, path):
            if not root:
                return 0

            if not root.left and not root.right:
                return path * 10 + root.val
            else:
                return dfs(root.left, path * 10 + root.val) + dfs(root.right, path * 10 + root.val)

        return dfs(root, 0)