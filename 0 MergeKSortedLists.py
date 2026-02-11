# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [ 1->4->5, 1->3->4, 2->6 ] merging them into one sorted list: 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# The first option is to use a recursive function to merge two lists at a time until one list is left.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        def mergeLists(lists):
            print(lists)
            if len(lists) == 1:
                return lists
            elif len(lists) == 2:
                dummy = ListNode(0)
                current = dummy
                n1 = lists[0]
                n2 = lists[1]
                while n1 and n2:
                    if n1.val <= n2.val:
                        current.next = n1
                        n1 = n1.next
                    else:
                        current.next = n2
                        n2 = n2.next
                    current = current.next

                if n1:
                    current.next = n1
                elif n2:
                    current.next = n2

                return [dummy.next]
            else:
                l = len(lists) // 2
                l1 = mergeLists(lists[:l])
                l2 = mergeLists(lists[l:])
                return mergeLists(l1 + l2)

        result = mergeLists(lists)
        return result[0] if len(result) > 0 else None

# The other option is to merge every two lists at a time with a while loop until one list is left.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))
            lists = temp
        
        return lists[0]
    
    def merge_lists(self, l1, l2):
        node = ListNode()
        ans = node
        
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        
        if l1:
            node.next = l1
        else:
            node.next = l2
        
        return ans.next