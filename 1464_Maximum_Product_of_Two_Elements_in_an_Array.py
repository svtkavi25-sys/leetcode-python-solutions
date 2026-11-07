class Solution(object):
    def maxProduct(self, nums):
        n=sorted(nums)
        result=0
        if len(n)>0:
            result=(n[len(n)-1]-1)*(n[len(n)-2]-1)
        return result
