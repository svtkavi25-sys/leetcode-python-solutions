class Solution(object):
    def intersect(self, nums1, nums2):
        result = list((Counter(nums1) & Counter(nums2)).elements())
        return result
