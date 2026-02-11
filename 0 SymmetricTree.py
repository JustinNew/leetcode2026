# https://leetcode.com/problems/symmetric-tree/
# Do level order traversal and check if the values are symmetric
# If the values are symmetric, then the tree is symmetric
# If the values are not symmetric, then the tree is not symmetric

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        levels = []
        levels.append(root)

        while levels:
            nodes = []
            values = []

            for n in levels:
                if n.left:
                    nodes.append(n.left)
                    values.append(n.left.val)
                else:
                    values.append(None)

                if n.right:
                    nodes.append(n.right)
                    values.append(n.right.val)
                else:
                    values.append(None)

            if values == values[::-1]:
                levels = nodes
            else:
                return False

        return True
    
# Recursive solution
class Solution(object):
    def isSymmetric(self, root):
        # Special case...
        if not root:
            return True
        # Return the function recursively...
        return self.isSame(root.left, root.right)
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        # If both root nodes are null pointers, return true...
        if leftroot == None and rightroot == None:
            return True
        # If exactly one of them is a null node, return false...
        if leftroot == None or rightroot == None:
            return False
        # If root nodes haven't same value, return false...
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)