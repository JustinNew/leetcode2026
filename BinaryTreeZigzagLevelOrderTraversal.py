# 103. Binary Tree Zigzag Level Order Traversal
# Very similar to 102. Binary Tree Level Order Traversal.
# Using a reverse flag in addition to the 102 solution.

# Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

from collections import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right    
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def reverse(list):
            l = 0
            r = len(list) - 1
            while l <= r:
                list[l], list[r] = list[r], list[l]
                l += 1
                r -= 1
            return

        result = []
        nodes = [root]
        while nodes:
            temp = []
            level = []
            for n in nodes:
                temp.append(n.val)
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)

            result.append(temp)
            nodes = level

        flag = 1
        for i in range(len(result)):
            if flag == -1:
                reverse(result[i])
            flag = flag * -1

        return result