class Solution(object):
    def isPowerOfThree(self, n):
        result=False
        for i in range(31):
            if (3**i)==n:
                result=True
            if (3**i)>n:
                break
        return result
