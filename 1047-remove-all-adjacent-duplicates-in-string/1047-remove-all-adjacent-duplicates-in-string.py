from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        str_stk = []
        for ch in s:
            if not str_stk or str_stk[-1] != ch:
                str_stk.append(ch)
            else:
                str_stk.pop()
        return ''.join(str_stk)