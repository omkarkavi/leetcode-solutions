class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node,left,right):
            if not node:
                return True

            if not (node.val > left and node.val < right):
                return False

            return helper(node.left,left,node.val)  and helper(node.right,node.val,right)
        return helper(root,float('-inf'),float('inf'))