class Solution(object):
    def vowelConsonantScore(self, s):
        c=0
        v=0
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                v+=1
            elif s[i].isalpha():
                c+=1
        if c!=0:
            return int(floor(v/c))
        else:
            return 0
