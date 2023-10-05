class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        n = set(nums)
        for i in nums:
            if i-1 not in n:
                count = 0
                while i in n:
                    count =count+1
                    i = i+1
                maxLen = max(maxLen,count)
        
        return maxLen
                    