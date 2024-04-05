class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        stk = [s[0]]
        while i<len(s):
            curr_ord = ord(s[i])
            if stk:
                last_ord = ord(stk[-1])
                if curr_ord+32 == last_ord or curr_ord-32 == last_ord:
                    stk.pop()
                else:
                    stk.append(s[i])
            else:
                stk.append(s[i])
            i += 1
        return ''.join(stk)