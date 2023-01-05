class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        res = [points[0]]
        # print(points)
        for x1, x2 in points[1:]:
            if res[-1][0] <= x1 <= res[-1][1]:
                res[-1][0] = max(res[-1][0], x1)
                res[-1][1] = min(res[-1][1], x2)
            else:
                res.append([x1, x2])
        
        # print(res)
        return len(res)