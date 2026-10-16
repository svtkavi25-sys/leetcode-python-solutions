class Solution(object):
    def reversePrefix(self, s, k):
        rev=s[(k-1)::-1]
        ori=s[k:]
        return  rev+ori
        
