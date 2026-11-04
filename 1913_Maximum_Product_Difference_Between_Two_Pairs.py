class Solution(object):
    def maxProductDifference(self, nums):
        n=sorted(nums)
        p=0
        if len(nums)>0:
            p=(n[len(n)-1]*n[len(n)-2])-(n[0]*n[1])
        return p
