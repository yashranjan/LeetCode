class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0
        
        while len(sticks)>1:
            f = heapq.heappop(sticks)
            s = heapq.heappop(sticks)
            ans += f+s
            heapq.heappush(sticks, f+s)
        
        return ans