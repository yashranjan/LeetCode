class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        prefix = [-1]*n
        suffix = [n]*n
        for i in range(1, n):
            if seats[i-1]:
                prefix[i] = i-1
            else:
                prefix[i] = prefix[i-1]
        for i in range(n-2, -1, -1):
            if seats[i+1]:
                suffix[i] = i+1
            else:
                suffix[i] = suffix[i+1]
        ans = 0
        for i in range(n):
            if seats[i] == 0:
                minSeat = math.inf
                if prefix[i] == -1:
                    minSeat = suffix[i]-i
                elif suffix[i] == n:
                    minSeat = i-prefix[i]
                else:
                    minSeat = min((i-prefix[i], suffix[i]-i))
                ans = max(ans, minSeat)
        return ans
        