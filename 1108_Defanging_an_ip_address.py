class Solution(object):
    def defangIPaddr(self, address):
        new=address.split(".")
        text=""
        n=len(new)
        for i in range(n):
            if new[i].isdigit:
                text=text+new[i]
            if i<=(n-2):
                text=text+"[.]"
        return text


        