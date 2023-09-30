class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea=0
        l,r=0,len(height)-1
        while r!=l:
            if height[l]<height[r]:
                area=(r-l)*(height[l])
                l=l+1
                maxArea=max(area,maxArea)
            else:
                area=(r-l)*(height[r])
                r=r-1
                maxArea=max(area,maxArea)
                
        return maxArea