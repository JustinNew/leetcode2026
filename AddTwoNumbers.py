# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers
# Key is to read the numbers from the linked lists and add them together
# and to return the result as a linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ReadNum(l: Optional[ListNode]):
            result = []
            while l:
                result.append(l.val)
                l = l.next

            return result

        num1 = ReadNum(l1)
        num2 = ReadNum(l2)

        ll = min(len(num1), len(num2))

        carry = 0
        total = []
        for i in range(ll):
            t = num1[i] + num2[i] + carry
            total.append(t % 10)
            carry = t // 10

        if len(num1) == ll:
            for i in range(ll, len(num2)):
                t = carry + num2[i]
                total.append(t % 10)
                carry = t // 10
        else:
            for i in range(ll, len(num1)):
                t = carry + num1[i]
                total.append(t % 10)
                carry = t // 10

        if carry != 0:
            total.append(carry)

        def AddNode(list):
            if len(list) == 0:
                return None

            h = ListNode(list[-1])
            h.next = AddNode(list[:-1])

            return h

        return AddNode(total[::-1])

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addTwo(l1, l2, carry):
            if l1 is None and l2 is None and carry == 0:
                return None
            elif l1 is None and l2 is None and carry !=0:
                h = ListNode(carry)
                return h
            elif l1 is None:
                t = l2.val + carry
                h = ListNode(t % 10)
                h.next = addTwo(None, l2.next, t // 10)
            elif l2 is None:
                t = l1.val + carry
                h = ListNode(t % 10)
                h.next = addTwo(None, l1.next, t // 10)
            else:
                t = l1.val + l2.val + carry
                h = ListNode(t % 10)
                h.next = addTwo(l1.next, l2.next, t // 10)

            return h

        return addTwo(l1, l2, 0)