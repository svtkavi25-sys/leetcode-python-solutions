class Solution(object):
    def getSneakyNumbers(self, nums):
        result=[]
        for i in set(nums):
            if nums.count(i)==2:
                result.append(i)
        return result
