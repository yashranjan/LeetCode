class Solution:
    def maxDepth(self, s: str) -> int:        
        cnt = 0
        ans = 0
        for i in s:
            if i == '(':
                cnt += 1
            elif i == ')':
                ans = max(ans, cnt)
                cnt -= 1
            else:
                continue
        return ans