class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r,w,b=0,0,0
        for i in nums:
            if i==0:
                r=r+1
            elif i==1:
                w=w+1
            else:
                b=b+1
                
        nums[:r]= [0] * r
        nums[r:r+w]= [1] * w
        nums[r+w:]= [2] * b