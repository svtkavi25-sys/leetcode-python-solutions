class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        add=0
        for i in str(x):
            add+=int(i)
        if x%add==0:
            return add
        else:
            return -1
        
