class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r=0,1
        currPrice,maxPrice=0,0
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r 
            
            elif prices[r]>=prices[l]:
                
                maxPrice=maxPrice+prices[r]-prices[l]
                l=l+1
            r=r+1
        
        return maxPrice