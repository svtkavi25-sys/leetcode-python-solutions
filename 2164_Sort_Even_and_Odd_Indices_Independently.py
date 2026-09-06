class Solution(object):
    def sortEvenOdd(self, nums):
        en=[]
        on=[]
        result=[]
        for i in range(len(nums)):
            if i%2==0:
                en.append(nums[i])
            else:
                on.append(nums[i])
        en.sort()
        on.sort(reverse=True)
        for i in range(len(en)):
            result.append(en[i])
            if i < len(on):
                result.append(on[i])
        if len(on) > len(en):
            result.append(on[-1])
        return result
