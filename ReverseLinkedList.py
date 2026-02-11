from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    nextNode = head.next
    head.next = None
    previousNode = head

    while nextNode.next:
        nextnextNode = nextNode.next

        nextNode.next = previousNode
        previousNode = nextNode
        nextNode = nextnextNode

    nextNode.next = previousNode

    return nextNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        previous = None
        current = head
        while current.next:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        current.next = previous

        return current