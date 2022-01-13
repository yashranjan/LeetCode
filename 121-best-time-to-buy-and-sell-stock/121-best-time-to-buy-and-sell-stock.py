class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minValue = prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i]-minValue)
            minValue = min(minValue, prices[i])
        return ans
        