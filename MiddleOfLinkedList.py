from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Two pointers approach
# One slow pointer and one fast pointer
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    if fast.next and fast.next.next is None :
        return slow.next
    elif fast.next is None:
        return slow