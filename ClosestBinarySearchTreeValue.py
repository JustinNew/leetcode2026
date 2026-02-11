# 270. Closest Binary Search Tree Value

# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

# Example:
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val

        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest 
    
# Example usage:
# Create a binary search tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Create a solution object
solution = Solution()
print(solution.closestValue(root, 4.154286))