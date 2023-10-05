class Solution(object):
    def maxProfit(self, prices):
        l,r=0,1
        currPrice,maxPrice=0,-1
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r   
            elif prices[r]>prices[l]:
                currPrice=prices[r]-prices[l]
                maxPrice=max(maxPrice,currPrice)
            r=r+1
        if maxPrice==-1:
            maxPrice=0
        return maxPrice