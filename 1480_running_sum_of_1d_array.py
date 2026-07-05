class Solution(object):
     
    def runningSum(self, nums):
        self.nums=nums
        arr=[]
        sum=0
        for i in range (len(nums)): 
            sum+=nums[i]
            arr.append(sum)

        return arr
                

        