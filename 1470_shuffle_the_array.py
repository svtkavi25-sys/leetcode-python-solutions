class Solution(object):
    def shuffle(self, nums, n):
         
        arr1=[]
        arr2=[]
        final=[]
        for i in range(0,n):
            arr1.append(nums[i])
        for j in range(n,len(nums)):
            arr2.append(nums[j])
        for i in range(n):
            final.append(arr1[i])
            final.append(arr2[i])
        return final

