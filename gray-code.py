class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n== 1:
            return [0,1]
        a = self.grayCode(n-1)
        s = []
        fact = 2**(n-1)
        for i in a[-1::-1]:
            s.append(i + fact )
        return a + s