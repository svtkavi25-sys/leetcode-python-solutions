class Solution(object):
    def sortedSquares(self, nums):
        squares=list(map(lambda x:x**2,nums))
        squares.sort()
        return squares
           
