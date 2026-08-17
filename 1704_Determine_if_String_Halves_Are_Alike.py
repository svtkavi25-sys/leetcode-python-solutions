class Solution(object):
    def halvesAreAlike(self, s):
        n=len(s)/2
        s1=s[:n]
        s2=s[n:]
        c1=0
        c2=0
        for i in range(len(s1)):
            if s1[i]=="a" or s1[i]=="e" or s1[i]=="i" or s1[i]=="o" or s1[i]=="u" or s1[i]=="A" or s1[i]=="E" or s1[i]=="I" or s1[i]=="O" or s1[i]=="U" :
                c1+=1
        for i in range(len(s2)):
            if s2[i]=="a" or s2[i]=="e" or s2[i]=="i" or s2[i]=="o" or s2[i]=="u" or s2[i]=="A" or s2[i]=="E" or s2[i]=="I" or s2[i]=="O" or s2[i]=="U" :
                c2+=1
        if c1==c2:
            return True
        else:
            return False
