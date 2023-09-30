# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        r = None
        p = None
        c = 0
        while l1 or l2 or c != 0:
            v = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            c = v // 10
            n = ListNode(v % 10)
            if r is None:
                r = n
            if p is not None:
                p.next = n
            p = n
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return r