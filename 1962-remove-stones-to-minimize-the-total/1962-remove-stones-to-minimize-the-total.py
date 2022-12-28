class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)
        while k:
            top = -heapq.heappop(piles)
            top -= top//2
            heapq.heappush(piles, -top)
            k -= 1
        
        return -sum(piles)
            