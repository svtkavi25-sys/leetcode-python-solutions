class Solution(object):
    def recoverOrder(self, order, friends):
        result=[]
        for i in range(len(order)):
            for j in range(len(friends)):
                if order[i]==friends[j]:
                    result.append(order[i])
        return result
