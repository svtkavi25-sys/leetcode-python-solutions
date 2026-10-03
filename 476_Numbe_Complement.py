class Solution(object):
    def findComplement(self, num):
        n1=bin(num)[2:]
        result=""
        for i in str(n1):
            if i=="0":
                result+="1"
            else:
                result+="0"
        final=int(result,2)
        return final
        
