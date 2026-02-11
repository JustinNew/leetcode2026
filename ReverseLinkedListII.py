# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseLinkedList(head):
        if head is None:
            return head

        if head.next is None:
            return head

        previous = head
        current = head.next
        nextNode = current.next
        previous.next = None

        while nextNode:
            current.next = previous

            previous = current
            current = nextNode
            nextNode = nextNode.next

        current.next = previous

        return current

class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head is None:
            return head

        if left == right:
            return head

        dummy = ListNode()
        dummy.next = head
        counter = 0
        previous = dummy

        while head:
            counter += 1

            if counter == left: 
                connectHeadNode = previous
                reverseHeadNode = head

            if counter == right:
                reverseEndNode = head
                connectTailNode = head.next

            previous = head
            head = head.next
            
        reverseEndNode.next = None

        # Reverse linked list
        newHeadNode = reverseLinkedList(reverseHeadNode)

        connectHeadNode.next = newHeadNode
        reverseHeadNode.next = connectTailNode

        return dummy.next

# Second time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseLinkedList(head: Optional[ListNode]):
    if not head or not head.next:
        return
    
    dummy = ListNode()
    dummy.next = head

    previous = None
    current = head
    nextn = current.next

    while current.next:
        current.next = previous

        previous = current
        current = nextn
        nextn = nextn.next

    current.next = previous

    return 

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head

        if left == right:
            return head

        dummy = ListNode()
        dummy.next = head

        connectTail = None
        connectHead = None

        revertHead = None
        revertTail = None

        previous = dummy
        
        count = 1
        while head:
            if count == left:
                revertHead = head
                connectTail = previous
            elif count == right:
                revertTail = head
                connectHead = head.next

            previous = head 
            head = head.next
            count += 1

        # Reset revertTail before reverse.
        if revertTail:
            revertTail.next = None
        print(revertHead.val)
        print(revertTail.val)
        reverseLinkedList(revertHead)

        if connectTail:
            connectTail.next = revertTail
        revertHead.next = connectHead

        return dummy.next