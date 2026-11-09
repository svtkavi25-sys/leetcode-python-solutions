class Solution(object):
    def findDuplicates(self, nums):
        seen = set()
        result=[]
        for num in nums:
            if num in seen:
                result.append(num)   
            else:
                seen.add(num)
        return result
