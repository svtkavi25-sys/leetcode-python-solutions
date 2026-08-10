class Solution(object):
    def reversePrefix(self, word, ch):
        r=""
        n=""
        result=""
        for i in range(len(word)):
            if ch in word:
                if word[i]==ch:
                    r+=ch
                    for j in range(i+1,len(word)):
                        n+=word[j]
                    break
                else:
                    r+=word[i]
            else:
                return word
            
        rev=r[::-1]
        result=rev+n
        return result
        
