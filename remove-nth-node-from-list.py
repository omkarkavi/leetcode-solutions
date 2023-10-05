# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nth=0
        
        fast=slow =head
        
      
        
        for i in range(n):
            fast=fast.next
            
        '''
        while nth<n:
            fast=fast.next
            nth=nth+1
            
       
       '''
       
        if not fast:
            return head.next
        
        while fast.next:
            fast=fast.next
            slow=slow.next
            
        slow.next=slow.next.next
        
        return head