class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        stk = [s[0]]
        while i<len(s):
            if not stk:
                stk.append(s[i])
            elif abs(ord(s[i]) - ord(stk[-1])) == 32:
                stk.pop()
            else:
                stk.append(s[i])
            i += 1
        return ''.join(stk)