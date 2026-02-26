# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Key is to use a pre-order traversal to flatten the tree.
# Then, connect the nodes in the pre-order traversal.

# Example 1:
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [0]
# Output: [0]

# DFS, Pre-order traversal
# Store the nodes in a list
# Connect the nodes in the list
# Return the root of the tree

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Do a pre-order traversal first
        # Then, connect them

        s = []

        def dfs(root):
            if not root:
                return
            
            s.append(root)
            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)

        for i in range(1, len(s)):
            s[i - 1].right = s[i]
            s[i - 1].left = None

        return

# This approach processes the tree in reverse post-order (right → left → root). 
# It ensures that we directly link the nodes in the desired "linked list" order.
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        # Process right subtree first
        self.flatten(root.right)

        # Process left subtree
        self.flatten(root.left)

        # Set the current node's right to prev and left to null
        root.right = self.prev
        root.left = None

        # Update prev to current node
        self.prev = root
