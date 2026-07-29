class Solution(object):
    def hammingWeight(self, n):
        b=(bin(n))
        count=0
        for ch in b:
            if ch=="1":
                count=count+1
        return count

        