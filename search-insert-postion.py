class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l,r = 0,len(nums)
        if target < nums[l]:
            return l
        if target > nums[r-1]:
            return r
        mid  = (l + r)//2
        while l<r:
            
            if target > nums[mid]:
                l = mid +1
            else:
                r = mid 
            mid  = (l + r)//2
        return l