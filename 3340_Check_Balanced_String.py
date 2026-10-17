class Solution(object):
    def isBalanced(self, num):
        evensum=0
        oddsum=0
        for i in range(len(num)):
            if i%2==0:
                evensum+=int(num[i])
            else:
                oddsum+=int(num[i])
        return evensum==oddsum
