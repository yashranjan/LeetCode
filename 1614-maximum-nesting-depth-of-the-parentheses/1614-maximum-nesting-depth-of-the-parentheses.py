class Solution:
    def maxDepth(self, s: str) -> int:
        stk = []
        
        cnt = 0
        ans = 0
        for i in s:
            if i == '(':
                stk.append(i)
                cnt += 1
            elif i == ')' and stk and stk[-1] == '(':
                ans = max(ans, cnt)
                stk.pop()
                cnt -= 1
            else:
                continue
        return ans