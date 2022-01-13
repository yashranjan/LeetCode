class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = []
        ans.append(points[0])
        for i in points[1:]:
            st, et = i[0], i[1]
            prevPoint = ans[len(ans)-1]
            if prevPoint[0] <= st <= prevPoint[1]:
                prevPoint[0] = max(prevPoint[0], st)
                prevPoint[1] = min(prevPoint[1], et)
            else:
                ans.append(i)
        print(ans)
        return len(ans)
        