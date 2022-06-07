class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x:x[0])
        
        ans.append(intervals[0])

        n = len(intervals)
        for i in range(1, n):
            currS, currE = intervals[i][0], intervals[i][1]
            lastInterval = ans[-1]
            print(lastInterval, currS, currE)
            if lastInterval[0]<=currS<=lastInterval[1] or lastInterval[0]<=currE<=lastInterval[1]:
                lastInterval[0] = min(lastInterval[0], currS)
                lastInterval[1] = max(lastInterval[1], currE)
            else:
                ans.append(intervals[i])
        return ans