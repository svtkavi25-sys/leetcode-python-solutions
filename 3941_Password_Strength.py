class Solution(object):
    def passwordStrength(self, password):
        p=[]
        m=0
        for i in password:
            p.append(i)
        s=list(set(p)) 
        for i in range(len(s)):
            if s[i].isalpha() and s[i].islower():
                m+=1
            elif s[i].isalpha() and s[i].isupper():
                m+=2
            elif s[i].isdigit():
                m+=3
            else:
                m+=5
        return m
