# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Key is to use a queue to store the nodes at each level and add the first node at each level to the result list.
# Then, add the right and left children of the nodes at each level to the queue.
# Finally, return the result list.

# example:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        nodes = [root]

        while nodes:
            level_nodes = []
            for i in range(len(nodes)):
                if i == 0:
                    result.append(nodes[i].val)
                
                if nodes[i].right:
                    level_nodes.append(nodes[i].right)
                if nodes[i].left:
                    level_nodes.append(nodes[i].left)

            nodes = level_nodes

        return result

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        def dfs_inorder(root, depth):
            if not root:
                return
            
            if depth == len(result):
                result.append(root.val)

            dfs_inorder(root.right, depth + 1)
            dfs_inorder(root.left, depth + 1)

        dfs_inorder(root, 0)

        return result
