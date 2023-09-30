class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        while l<= r:
            if nums[l] != target:
                l = l +1
            else:
                break
        while l<= r:
            if nums[r] != target:
                r = r -1
            else:
                break
        if l>r:
            return [-1,-1]
        return  [l,r]             
                