class Solution(object):
    def isPowerOfTwo(self, n):
        result=False
        if n<=0:
            result=False
        elif n==1:
            result=True
        else:
            for i in range(31):
                if n==(2**i):
                    result=True
                if (2**i)>n:
                    break
        return result
        
