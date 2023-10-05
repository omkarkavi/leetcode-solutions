import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Just use the formula and save headache
        return math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))