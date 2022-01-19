class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSeenSoFar = prices[0]
        ans = 0
        for i in prices[1:]:
            ans = max(ans, i-minSeenSoFar)
            minSeenSoFar = min(minSeenSoFar, i)
        return ans