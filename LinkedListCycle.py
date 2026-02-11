from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return False

    heap = []
    while head:
        if head in heap:
            return True

        heap.append(head)
        head = head.next

    return False

def hasCycle2(head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False