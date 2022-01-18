class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(2, numRows+1):
            curr = [1]
            prevI = 0
            while prevI < len(ans[-1])-1:
                curr.append(ans[-1][prevI]+ans[-1][prevI+1])
                prevI += 1
            curr.append(1)
            ans.append(curr)
        return ans
        