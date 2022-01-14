class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        isNegative = False
        if s[0]=='-' or s[0]=='+':
            if s[0] == '-': isNegative = True
            s = s[1:]
        t = []
        for i in s:
            if i.isdigit():
                t.append(i)
            else:
                break
        if not t:
            return 0
        val = int(''.join(t))
        if isNegative:
            val = -val
        intMin, intMax = -2**31, 2**31-1
        val = max(intMin, val)
        val = min(intMax, val)
        return val