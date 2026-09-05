class Solution(object):
    def addToArrayForm(self, num, k):
        s=""
        ra=[]
        for i in range(len(num)):
            s+=str(num[i])
        result=int(s)+k
        for i in str(result):
            ra.append(int(i))
        return ra
