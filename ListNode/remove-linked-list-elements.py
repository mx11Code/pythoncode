# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return dummy