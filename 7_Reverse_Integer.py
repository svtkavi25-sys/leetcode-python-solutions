class Solution(object):
    def reverse(self, x):
        n=-2**31
        m=2**31-1
        if x<0:
            y=(-1)*x
            xs=str(y)[::-1]
            if n<=int(xs)<=m:
                return -1*int(xs)
            else:
                return 0
        else:
            xs=str(x)[::-1]
            if n<=int(xs)<=m:
                return int(xs)
            else:
                return 0
         
