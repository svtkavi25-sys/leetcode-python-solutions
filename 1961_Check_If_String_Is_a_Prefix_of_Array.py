class Solution(object):
    def isPrefixString(self, s, words):
        s1=""
        for i in range(len(words)):
            s1+=words[i]
            if s1==s:
                break
        if s1==s:
            return True
        else:
            return False
