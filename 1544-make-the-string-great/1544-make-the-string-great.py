class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i+1<len(s):
            c, n = ord(s[i]), ord(s[i+1])
            if c+32 == n or c-32 == n:
                s = s[:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i += 1
        return s