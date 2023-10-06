# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow=head
        
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        prev=None
        while mid:
            tmp=mid.next
            mid.next=prev
            prev=mid
            mid=tmp
        first,second=head,prev
        while second:
            tmp=second.next
            tpp=first.next
            first.next=second
            second.next=tpp
            second=tmp
            first=tpp