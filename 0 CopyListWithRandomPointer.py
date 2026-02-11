# 138. Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has a value equal to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
# Key is to use a hash map to store the original nodes and the copied nodes.
# Then, iterate through the original list and copy the nodes with next and random pointers.
# Finally, return the head of the copied list.

# example:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# example:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# example:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Copy the list with next first.
# Use two hash maps to store the original nodes and the copied nodes.
# Then, iterate through the original list and copy the nodes with next and random pointers.
# Finally, return the head of the copied list.

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        d1 = {}
        d2 = {}
        current = dummy
        head1 = head
        count = 1

        # Copy the list with next
        while head:
            current.next = Node(head.val)
            d1[head] = count
            d2[count] = current.next
            head = head.next
            current = current.next
            count += 1

        # Copy random
        head = head1
        current = dummy.next
        while head:
            if head.random == None:
                current.random = None
            else:
                current.random = d2[d1[head.random]] 
            head = head.next
            current = current.next

        return dummy.next

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]