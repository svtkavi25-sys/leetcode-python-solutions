class Solution(object):
    def getCommon(self, nums1, nums2):
        new=list(set(nums1) & set(nums2))
        new.sort()
        if len(new)==0:
            return -1
        else:
            return new[0]
