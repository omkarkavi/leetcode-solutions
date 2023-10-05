class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        strt = 1
        while strt in nums:
            strt =strt +1
        return strt