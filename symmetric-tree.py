# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.isSameTreeReverse(root.left,root.right) 
        
        
    #Check if the binary tree is same on left side and right side
    def isSameTreeReverse(self, p, q):
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            return self.isSameTreeReverse(p.left, q.right) and self.isSameTreeReverse(p.right, q.left)

        return False