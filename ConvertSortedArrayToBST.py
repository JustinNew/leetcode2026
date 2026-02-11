# Definition for a binary tree node.
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Recursion approach

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            n = TreeNode(nums[0])
            return n

        mid = len(nums) // 2
        n = TreeNode(nums[mid])
        n.left = self.sortedArrayToBST(nums[:mid])
        n.right = self.sortedArrayToBST(nums[mid + 1:])

        return n