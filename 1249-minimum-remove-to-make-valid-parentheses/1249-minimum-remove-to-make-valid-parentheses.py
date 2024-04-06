class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_lst = list(s)
        stk = []
        
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stk.append(i)
            elif char == ')':
                if stk:
                    stk.pop()
                else:
                    s_lst[i] = ''
        
        while stk:
            s_lst[stk.pop()] = ''
        
        return ''.join(s_lst)