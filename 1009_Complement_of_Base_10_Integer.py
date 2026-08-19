class Solution(object):
    def bitwiseComplement(self, n):
        n1=bin(n)[2:]
        c1=""
        for i in range(len(str(n1))):
            if n1[i]=="0": 
                c1+="1"
            else:
                c1+="0"
        return int(c1,2) 
        
