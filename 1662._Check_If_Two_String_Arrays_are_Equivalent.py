class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        w1=""
        w2=""
        for ch in word1:
            w1+=ch
        for ch in word2:
            w2+=ch
        if w1==w2:
            return True
        else:
            return False
        