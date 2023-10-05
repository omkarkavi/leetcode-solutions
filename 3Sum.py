class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finnums=[]
        nums.sort()
        for i, a in enumerate(nums):
            if a == nums[i-1] and i>0:
                continue
            l,r = i+1,len(nums) -1
            while l<r:
                thsum = a + nums[l]  + nums[r]
                if thsum < 0:
                    l = l+1
                elif thsum>0:
                    r = r-1
                else:
                    finnums.append([a , nums[l]  , nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
        return finnums