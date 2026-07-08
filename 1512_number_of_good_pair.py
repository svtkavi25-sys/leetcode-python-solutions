class Solution(object):
    def numIdenticalPairs(self, nums):
        pair=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    p=[(i,j)]
                    pair.append(p)
        return len(pair)

        