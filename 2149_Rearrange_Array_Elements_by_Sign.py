class Solution(object):
    def rearrangeArray(self, nums):
        n=[]
        p=[]
        result=[]
        for i in range(len(nums)):
            if nums[i]<0:
                n.append(nums[i])
            else:
                p.append(nums[i])
        for a, b in zip(p,n):
            result.append(a)
            result.append(b)
        return result
