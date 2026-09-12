class Solution(object):
    def firstPalindrome(self, words):
        revarr=[]
        result=""
        for i in range(len(words)):
            revarr.append(words[i][::-1])
        for i in range(len(words)):
            if len(result)<1:
                if words[i]==revarr[i]:
                    result+=words[i]
        return result
        
