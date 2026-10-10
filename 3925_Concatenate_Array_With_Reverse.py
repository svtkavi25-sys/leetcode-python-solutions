class Solution(object):
    def concatWithReverse(self, nums): 
        reverse=nums[::-1]
        nums.extend(reverse)
        return nums
