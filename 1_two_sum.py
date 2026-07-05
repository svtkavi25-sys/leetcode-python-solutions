class Solution(object):
    def twoSum(self, nums, target):
         self.nums=nums
         self.target=target
         for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                    return i,j
        