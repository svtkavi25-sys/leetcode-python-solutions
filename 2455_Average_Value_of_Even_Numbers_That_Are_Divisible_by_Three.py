class Solution(object):
    def averageValue(self, nums):
        total=[]
        tot=0
        for i in range(len(nums)):
            if nums[i]%3==0 and nums[i]%2==0:
                total.append(nums[i])
        for i in range(len(total)):
            tot+=total[i]
        if tot==0:
            return 0
        else:   
            return tot/len(total)
