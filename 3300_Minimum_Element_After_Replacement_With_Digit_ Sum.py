class Solution(object):
    def minElement(self, nums):
        nums1=[]
        for i in range(len(nums)):
            if len(str(nums[i]))>1:
                add=0
                for j in str(nums[i]):
                    add+=int(j)
                nums1.append(add)
            else:
                nums1.append(nums[i])
        nums1.sort()
        if len(nums1)!=0:
            return nums1[0]
        else:
            return -1
