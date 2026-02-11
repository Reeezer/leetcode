from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # O(max(m, n))
        head = ListNode()
        current = head
        carry = 0
        while l1 or l2 or carry:
            # Sum values (on the fly)
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            # Update to List and carry
            carry = val // 10
            current.next = ListNode(val % 10)
            current = current.next

        return head.next
