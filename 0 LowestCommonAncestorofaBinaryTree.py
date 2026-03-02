# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Key is to use a DFS to find the LCA.
# We can then return the LCA.
# We can then use a helper function to find the LCA.
# We can then use a helper function to find the LCA.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This solution will TLE.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root, n):
            if not root:
                return False

            if root == n:
                return True

            return dfs(root.left, n) or dfs(root.right, n)

        current = root
        while current:
            if current == p or current == q:
                return current
            else:
                if dfs(current.left, p) and dfs(current.left, q):
                    current = current.left
                elif dfs(current.right, p) and dfs(current.right, q):
                    current = current.right
                else:
                    return current

# DFS to get the path.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root, n, path):
            if root == n:
                path.append(root)
                return True

            path.append(root)
            if root.left:
                if dfs(root.left, n, path):
                    return True
            if root.right:
                if dfs(root.right, n, path):
                    return True
            path.pop()

            return False

        p_path = [] 
        q_path = []
        dfs(root, p, p_path)
        dfs(root, q, q_path)

        for i in range(min(len(p_path), len(q_path))):
            if i > 0 and p_path[i] != q_path[i]:
                return p_path[i - 1]

        return p_path[min(len(p_path), len(q_path)) - 1]

# DFS to get the LCA.
# This is the best solution.
# Need to understand the logic.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right  

        