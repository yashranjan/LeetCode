class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        ans = [[0]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                ans[j][n-i-1] = matrix[i][j]
        matrix[:]=ans
        # print(ans)