class Solution(object):
    def separateDigits(self, nums):
        s=str(nums) 
        result=""
        answer=[]
        for i in range(len(s)):
            if s[i]!="," and s[i]!="[" and s[i]!="]" and s[i]!=" ":
                result+=s[i]
        for i in result:
            answer.append(int(i))
        return answer
        
