class Solution(object):
    def restoreString(self, s, indices):
        sindices = dict(zip(indices,s))
        result = "".join(sindices.values())
        return str(result)
