class Solution(object):
    def findPeakElement(self, nums):
        maximum=nums[0]
        if len(nums)==0 or len(nums)==1:
            return 0
        else:
            
            for i in range(len(nums)):
                if maximum<nums[i]:
                    maximum=nums[i]
            for i in range(len(nums)):
                if maximum==nums[i]:
                    return i
        
