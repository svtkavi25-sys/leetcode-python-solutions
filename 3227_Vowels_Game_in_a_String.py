class Solution(object):
    def doesAliceWin(self, s):
        vowel=[]
        for i in range(len(s)):
            if s[i].lower()=="a" or s[i].lower()=="e"or s[i].lower()=="i" or s[i].lower()=="o" or s[i].lower()=="u":
                vowel.append(s[i])
        if len(vowel)==0:
            return False
        else:
            return True
