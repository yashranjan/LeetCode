class Solution:
    def searchRows(self, matrix, target, row, col):
        st = 0
        et = row
        ans = 0
        while st <= et:
            mid = (st+et)//2
            if matrix[mid][col] >= target:
                ans = mid
                et = mid-1
            else:
                st = mid+1
        return ans
    
    def searchCols(self, matrix, target, row, col):
        st, et = 0, col
        while st<=et:
            mid = (st+et)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                et = mid-1
            else:
                st = mid+1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row = self.searchRows(matrix, target, n-1, m-1)
        return self.searchCols(matrix, target, row, m-1)