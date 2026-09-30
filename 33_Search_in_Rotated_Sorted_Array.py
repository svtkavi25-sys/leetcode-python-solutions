class Solution(object):
    def search(self, nums, target):
        result=[]
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
        if len(result)!=0:
            return result[0]
        else:
            return -1
        
