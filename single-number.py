class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ss1 =sum(nums)
        ss2 = sum(set(nums))
        
        return -ss1 + ss2 + ss2