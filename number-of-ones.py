class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        sum1=0
        while n!=0:
            sum1=sum1 + n%2
            n=n/2
            
            
        
            
            
        return sum1
        