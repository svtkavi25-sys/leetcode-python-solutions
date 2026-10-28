class Solution(object):
    def calculateScore(self, a, b):
        a1=bin(a)[2:]
        b1=bin(b)[2:]
        ca=0
        cb=0
        for i in str(a1):
            if i=="1":
                ca+=1
        for i in str(b1):
            if i=="1":
                cb+=1
        if ca>=cb:
            return ca*cb
        else:
            return cb/ca
