class Solution(object):
    def reverseWords(self, s):
        rev=""
        revarr=s.split(" ")
        for i in range(len(revarr)):
            if i==len(revarr)-1:
                rev+=revarr[i][::-1]
            else:
                rev=rev+revarr[i][::-1]+" "
        return rev
