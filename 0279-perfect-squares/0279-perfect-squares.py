class Solution:
    def numSquares(self, n):
        pre_sq_nums = [i*i for i in range(int(sqrt(n))+1)]
        
        dp = [10**5]*(n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for sq in pre_sq_nums:
                if sq>i:
                    break
                dp[i] = min(dp[i], dp[i-sq]+1)
        
        
        return dp[-1]