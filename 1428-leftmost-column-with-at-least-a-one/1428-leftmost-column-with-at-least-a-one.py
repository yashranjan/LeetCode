# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        def getOnePos(binaryMatrix, row, cols):
            l, r = 0, cols-1
            curr = float('inf')
            while l<=r:
                m = (l+r)//2
                val = binaryMatrix.get(row, m)
                if not val:
                    l = m+1
                else:
                    curr = m
                    r = m-1
            return curr
        
        ans = float('inf')
        
        rows, cols = binaryMatrix.dimensions()
        
        for row in range(rows):
            h = ans if ans!=float('inf') else cols
            ans = min(ans, getOnePos(binaryMatrix, row, h))
        
        return ans if not ans==float('inf') else -1