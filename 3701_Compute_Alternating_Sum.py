class Solution(object):
    def alternatingSum(self, nums):
        oddsum=0
        evensum=0
        for i in range(len(nums)):
            if i%2==0:
                evensum+=nums[i]
            else:
                oddsum+=nums[i]
        return evensum-oddsum
        
