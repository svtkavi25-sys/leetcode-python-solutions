class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count=0
        for i in range(nums):
           if len(str(i))>0:
               for j in str(i):
                   if int(j)==digit:
                       count+=1
           else:
               if i==digit:
                   count+=1
        return count         
