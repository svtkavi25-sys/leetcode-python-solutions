class Solution(object):
    def findNonMinOrMax(self, nums):
        n=sorted(nums)
        if len(nums)>2:
            return n[1]
        else:
            return -1
