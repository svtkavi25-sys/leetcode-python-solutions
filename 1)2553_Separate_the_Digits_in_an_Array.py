class Solution(object):
    def separateDigits(self, nums):
        result=[]
        for i in range(len(nums)):
            if len(str(nums[i]))>1:
                for j in str(nums[i]):
                    result.append(int(j))
            else:
                result.append(nums[i])
        return result
