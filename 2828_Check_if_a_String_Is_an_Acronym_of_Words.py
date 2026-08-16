class Solution(object):
    def isAcronym(self, words, s):
        result=""
        for i in words:
            result+=i[0]
        if result==s:
            return True
        else:
            return False

        
