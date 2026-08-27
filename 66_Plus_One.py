class Solution(object):
    def plusOne(self, digits):
        total=""
        final=""
        result=[]
        for i in digits:
            total+=str(i)
        final=int(total)+1
        for i in str(final):
            result.append(int(i))
        return result
