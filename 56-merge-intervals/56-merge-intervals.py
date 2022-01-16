class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x:x[0])
        ans.append(intervals[0])
        for st,et in intervals[1:]:
            prevSt, prevEt = ans[-1]
            if prevSt <= st <= prevEt:
                ans[-1][0] = min(prevSt, st)
                ans[-1][1] = max(prevEt, et)
            else:
                ans.append([st, et])
        return ans
                
        