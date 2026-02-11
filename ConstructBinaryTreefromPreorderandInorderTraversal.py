# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Recursive solution
# 1. The first element in preorder is the root
# 2. Find the root in inorder
# 3. The elements to the left of the root in inorder are in the left subtree
# 4. The elements to the right of the root in inorder are in the right subtree
# 5. Recursively build the left and right subtrees

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Recursive solution
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break
        
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root