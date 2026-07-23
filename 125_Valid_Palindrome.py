class Solution(object):
    def isPalindrome(self, s):
        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch.lower()

        if new == new[::-1]:
            return True
        else:
            return False