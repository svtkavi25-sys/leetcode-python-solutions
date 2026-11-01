class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        n1,n2,n3=set(nums1),set(nums2),set(nums3)
        result=(n1 & n2) | (n2 & n3) | (n1 & n3)
        return list(result)
