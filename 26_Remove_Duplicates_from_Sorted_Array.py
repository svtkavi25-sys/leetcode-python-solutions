class Solution(object):
    def removeDuplicates(self, nums):
        numsset=list(set(nums))
        numsset.sort()
        nums[:len(numsset)]=numsset
        return len(numsset)

            
        
