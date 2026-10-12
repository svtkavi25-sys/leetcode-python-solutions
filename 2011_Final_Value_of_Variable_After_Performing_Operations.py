class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for i in range(len(operations)):
            if operations[i]=="X++":
                x+=1
            elif operations[i]=="X--":
                x-=1
            elif operations[i]=="++X":
                x+=1
            else:
                x-=1
        return x
        
        
