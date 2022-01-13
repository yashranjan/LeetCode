class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        suffMax = prices[:]
        suffMax[len(prices)-1] = prices[len(prices)-1]
        for i in range(len(prices)-2, -1, -1):
            suffMax[i] = max(prices[i], suffMax[i+1])
        for i in range(len(prices)-1):
            ans = max(ans, suffMax[i+1]-prices[i])
        return ans
        