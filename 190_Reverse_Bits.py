class Solution(object):
    def reverseBits(self, n):
        r="{:032b}".format(n)
        r1=r[::-1]
        return int(r1,2)
