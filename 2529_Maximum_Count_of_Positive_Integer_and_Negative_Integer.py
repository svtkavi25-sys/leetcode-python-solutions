class Solution(object):
    def maximumCount(self, nums):
        pm=0
        nm=0
        for i in range(len(nums)):
            if nums[i]<0:
                nm+=1
            elif nums[i]==0:
                pass
            else:
                pm+=1
        if pm>nm:
            return pm
        else:
            return nm
