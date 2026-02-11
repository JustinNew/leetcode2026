# 116. Populate Next Right Pointers in Each Node
# https://leetcode.com/problems/populate-next-right-pointers-in-each-node/
# Key is to use a queue to store the nodes at each level and add the next pointer for each node.
# Then, add the left and right children of the nodes at each level to the queue.
# Finally, return the root of the tree.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]

# Key is to use a queue to store the nodes at each level and add the next pointer for each node.
# Then, add the left and right children of the nodes at each level to the queue.
# Finally, return the root of the tree.

# BFS solution
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        current = [root]
        while current:
            for i in range(len(current)):
                if i + 1 == len(current):
                    current[i].next = None
                else:
                    current[i].next = current[i + 1]

            temp = []
            for r in current:
                if r.left:
                    temp.append(r.left)
                    temp.append(r.right)
            
            current = temp

        return root

# Recursive solution

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
  def helper(self, root: 'Node', parent: 'Node') -> None:
    if root is None:
      return
    if parent is not None:
      parent.left.next = parent.right
    if parent is not None and parent.next is not None:
      parent.right.next = parent.next.left
    if root.left is None and root.right is None:
      return
    self.helper(root.left, root)
    self.helper(root.right, root)
  
  def connect(self, root: 'Node') -> 'Node':
    self.helper(root, None)
    return root