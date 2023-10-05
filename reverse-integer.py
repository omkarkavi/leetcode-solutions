class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        fact = 1
        if x< 0:
            fact = -1
            x = x*fact
        pp = 0
        while x>0:
            pp = pp*10 + x%10
            x = x//10
        if pp*fact >2**31-1 or pp*fact <-2**31:
            return 0
        else:
            return pp*fact