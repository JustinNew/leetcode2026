# 173. Binary Search Tree Iterator
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the next, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

# Example:
# Input:
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output:
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Key is to use a stack to store the nodes in the left subtree.
# Then, when next() is called, pop the top node from the stack and return its value.
# If the node has a right child, push the right child and all its left children to the stack.
# Finally, return the value of the node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val

# My solution:
# 1. Use a list to store the nodes in the in-order traversal.
# 2. Use a pointer to store the current index of the list.
# 3. Use a function to traverse the tree in-order and store the nodes in the list.
# 4. Use a function to return the next node in the in-order traversal.
# 5. Use a function to check if there is a next node in the in-order traversal.

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.l = []
        self.ndx = -1

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            self.l.append(root.val)
            dfs(root.right)

        dfs(root)

    def next(self) -> int:
        self.ndx += 1
        return self.l[self.ndx]

    def hasNext(self) -> bool:
        if self.ndx + 1 < len(self.l):
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# How to optimize the solution?
# 1. Use a stack to store the nodes in the left subtree.
# 2. Use a pointer to store the current index of the stack.
# 3. Use a function to traverse the tree in-order and store the nodes in the stack.
# 4. Use a function to return the next node in the in-order traversal.
# 5. Use a function to check if there is a next node in the in-order traversal.