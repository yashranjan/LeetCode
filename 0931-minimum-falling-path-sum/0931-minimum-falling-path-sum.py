class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        maxi = float('inf')
        prev_row = [maxi] + matrix[0][:] + [maxi]

        for i in range(1,len(matrix)):
            temp = []
            for j in range(len(matrix[0])):
                temp.append(matrix[i][j] + min(prev_row[j:j+3]))

            prev_row = [maxi]+temp+[maxi]
        
        return min(prev_row)