class Solution(object):
    def findDifference(self, nums1, nums2):
        a1=list(set(nums1)-set(nums2))
        a2=list(set(nums2)-set(nums1))
        result=[]
        result.append(a1)
        result.append(a2)
        return result
        
