class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        prev, future = math.inf, 0
        ans = 0
        for i in range(n):
            if seats[i]:
                prev = i
            else:
                if future <= i:
                    for j in range(i+1, n):
                        if seats[j]:
                            future = j
                            break
                    else:
                        future = math.inf
                leftSeat = i - prev if prev != math.inf else math.inf
                rightSeat = future - i if future != math.inf else math.inf
                ans = max(ans, min(leftSeat, rightSeat))
        
        return ans
        