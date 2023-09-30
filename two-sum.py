class Solution(object):
    def twoSum(self, nums, target):
        holder=[]
        for i in range(len(nums)):
            if target-nums[i] not in holder:
                holder.append(nums[i])
            else:
                return [i,nums.index(target-nums[i])]