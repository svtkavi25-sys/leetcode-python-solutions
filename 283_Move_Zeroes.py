class Solution(object):
    def moveZeroes(self, nums):
        new=[]
        zero=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                zero.append(nums[i])
            else:
                new.append(nums[i])
        update=new+zero
        for i in range(len(nums)):
            nums[i] = update[i]
        
        