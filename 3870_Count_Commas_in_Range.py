class Solution(object):
    def countCommas(self, n):
        sn=str(n)
        count=0
        if len(sn)<=3:
            return 0
        else:
            for i in range(1000,n+1):
                count+=1       
            return count
