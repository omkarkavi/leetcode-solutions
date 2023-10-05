# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        q=collections.deque()
        q.append(root)
        
        while q:
            eleLev=[]
            for i in range(len(q)):
                lee=q.popleft()
                
                if lee:
                    eleLev.append(lee.val)
                    q.append(lee.left)
                    q.append(lee.right)
            if len(eleLev)>0:
                result.append(eleLev)
        return result