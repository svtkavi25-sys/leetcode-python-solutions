class Solution(object):
    def applyOperations(self, nums):
        z=[],n=[],r=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        for i in range(len(nums)):
            if nums[i]==0:
                z.append(nums[i])
            else:
                n.append(nums[i])
        for i in range(len(n)):
            r.append(n[i])
        for i in range(len(z)):
            r.append(z[i])

        return r
        