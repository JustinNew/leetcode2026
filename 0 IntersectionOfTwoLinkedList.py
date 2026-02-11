from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Using stack
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    pass 

# Two pointers run through the two lists until the two pointers meet/equal
# If there are intersection, the two pointers will meet at the intersection node
# If there is no intersection, the two pointers will meet at the end of the two lists, a.k.a. None
def getIntersectionNode2(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    pass

