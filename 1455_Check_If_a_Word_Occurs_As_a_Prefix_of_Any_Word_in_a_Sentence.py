class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        s=sentence.split(" ")
        result=[]
        for i in range(0,len(s)):
            if s[i].startswith(searchWord):
                return i+1
                break
        return -1
