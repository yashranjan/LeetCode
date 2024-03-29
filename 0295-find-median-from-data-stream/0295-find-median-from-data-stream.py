class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo=[]
        self.hi=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return float(-self.lo[0] + self.hi[0]) / 2