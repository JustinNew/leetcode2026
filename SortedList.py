# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if head is None or head.next is None:
        return head

    largeNode = ListNode()
    largeNode.next = None
    largeDummy = largeNode

    smallNode = ListNode()
    smallNode.next = None
    smallDummy = smallNode

    pivot = head
    while head.next:
        head = head.next
        if head.val >= pivot.val:
            print('Assigning to large list.')
            largeNode.next = head
            largeNode = largeNode.next
        else:
            print('Assigning to small list.')
            smallNode.next = head
            smallNode = smallNode.next
    pivot.next = None
    if smallNode:
        smallNode.next = None
    if largeNode:
        largeNode.next = None

    print('Small List:')
    printList(smallDummy.next)
    print('Pivot:')
    printList(pivot)
    print('Large List:')
    printList(largeDummy.next)
    print('--------------------------------')

    if smallDummy.next is not None:
        smallNode = sortList(smallDummy.next)
    else:
        smallNode = None

    if largeDummy.next is not None:
        largeNode = sortList(largeDummy.next)
    else:
        largeNode = None

    return merge(smallNode, pivot, largeNode)

def merge(smallNode, pivot, largeNode):
    startNode = smallNode

    if smallNode is None:
        startNode = pivot
    else:
        while smallNode.next:
            smallNode = smallNode.next

        smallNode.next = pivot
    
    if largeNode is not None:
        pivot.next = largeNode

    print('Merged List:')
    printList(startNode)
    print('--------------------------------')
    print('--------------------------------\n\n')
    return startNode

def printList(head):
    if head is None:
        return
    
    while head:
        print(head.val)
        head = head.next
    return

node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

printList(sortList(node1))
