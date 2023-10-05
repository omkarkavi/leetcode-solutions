class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<= 1:
            return x
        l,r = 1, x
        
        while l<=r:
            mid = (l+r)//2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            if x < mid  ** 2:
                r = mid - 1
            else:
                l = mid + 1
               