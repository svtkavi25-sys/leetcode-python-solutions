class Solution(object):
    def findNumbers(self, nums):
        size=[]
        count=0
        for i in range(len(nums)):
            size.append(len(str(nums[i])))
        for i in range(len(size)):
            if size[i]%2==0:
                count+=1
        return count
        
