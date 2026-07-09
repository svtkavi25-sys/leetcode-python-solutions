class Solution(object):
    def mostWordsFound(self, sentences):
        arr=[]
        pair=[]
        maximum=0
        for i in sentences:
            arr=i.split()
            pair.append(len(arr))
         
        for i in range(len(pair)):
            for j in range(i+1,len(pair)):
                if pair[maximum]<=pair[j]:
                    maximum=j

        return pair[maximum]

