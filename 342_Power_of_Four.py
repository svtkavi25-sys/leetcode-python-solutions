class Solution(object):
    def isPowerOfFour(self, n):
        result=False
        if n==0 or n<0:
            return False
        elif n==1:
            return True
        else:
            for i in range(31):
                if n==(4**i):
                    result=True
                if (4**i)>n:
                    break
        return result
