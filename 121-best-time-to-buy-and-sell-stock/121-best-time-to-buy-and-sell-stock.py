class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = math.inf
        ans = -math.inf
        
        for price in prices:
            minSoFar = min(minSoFar, price)
            ans = max(ans, price-minSoFar)
        
        return ans