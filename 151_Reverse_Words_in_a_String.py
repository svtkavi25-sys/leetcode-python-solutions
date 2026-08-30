class Solution(object):
    def reverseWords(self, s):
        n=s.split(" ")
        r=n[::-1] 
        a=" ".join(" ".join(map(str,r)).split())
        return a
