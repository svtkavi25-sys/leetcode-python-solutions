class Solution(object):
    def subtractProductAndSum(self, n):
        s=str(n)
        mul=1
        add=0
        for i in range(len(s)):
            mul*=int(s[i])
            add+=int(s[i])
        return mul-add
        
