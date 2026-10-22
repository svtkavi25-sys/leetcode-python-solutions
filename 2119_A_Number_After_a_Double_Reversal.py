class Solution(object):
    def isSameAfterReversals(self, num):
        rev=int(str(num)[::-1])
        rev2=int(str(rev)[::-1]) 
        return rev2==num
        
