class Solution(object):
    def sumAndMultiply(self, n):
        if n==0:
            return 0
        else:
            s=""
            added=0
            m=str(n)
            for i in m:
                if i!="0":
                    s+=i
            for i in s:
                added+=int(i)
            result=int(s)*added
            return result 
