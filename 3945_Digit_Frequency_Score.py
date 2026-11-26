class Solution(object):
    def digitFrequencyScore(self, n):
        result=0
        for i in set(str(n)):
            result+=(int(i)*(str(n).count(i)))
        return result
