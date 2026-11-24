class Solution(object):
    def scoreValidator(self, events):
        result=0
        counter=0
        for i in events:
            if i=="W":
                counter+=1
                if counter==10:
                    break
            elif i=="WD" or i=="NB":
                result+=1
            else:
                result+=int(i)
        return [result,counter]
        
