class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r= 0
        cSum=0
        if len(nums)==1:
            return nums[0]
        cMax=nums[0]
        while r<len(nums):
            if cSum <= 0:
                cSum = 0
            cSum = cSum + nums[r]
            r=r+1
            cMax = max(cMax,cSum)
        return cMax
            