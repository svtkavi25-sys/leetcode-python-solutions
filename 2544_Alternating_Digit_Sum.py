class Solution(object):
    def alternateDigitSum(self, n):
        result=0
        m=str(n)
        for i in range(len(m)):
            if i%2==0:
                result+=int(m[i])
            else:
                result-=int(m[i])
        return result
