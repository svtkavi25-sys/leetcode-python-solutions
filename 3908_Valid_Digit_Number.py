class Solution(object):
    def validDigit(self, n, x):
        if str(n).startswith(str(x)):
            return False
        else:
            result=False
            if str(x)in str(n):
                result=True
            return result
        
