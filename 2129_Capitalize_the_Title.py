class Solution(object):
    def capitalizeTitle(self, title):
        t=title.split()
        result=""
        for i in range(len(t)):
            if len(t[i])>2:
                result+=t[i].capitalize()
            else:
                result+=t[i].lower()
            if i < len(t) - 1:
                result += " "
        return result
