class Solution(object):
    def isPalindromic(self, s):
        a=""
        for i in s:
            a+="0"
            a+=str(bin(ord(i))[2:]) 
        return a==a[::-1]
