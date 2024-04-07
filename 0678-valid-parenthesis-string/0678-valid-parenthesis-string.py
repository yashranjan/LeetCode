class Solution:
    def checkValidString(self, s: str) -> bool:
        brack_stk = []
        star_stk = []
        
        for idx, i in enumerate(s):
            if i == '(':
                brack_stk.append(idx)
            elif i == ')':
                if not brack_stk and not star_stk:
                    return False
                elif brack_stk:
                    brack_stk.pop()
                elif star_stk:
                    star_stk.pop()
            else:
                star_stk.append(idx)
        while brack_stk and star_stk:
            brack_idx, star_idx = brack_stk.pop(), star_stk.pop()
            if brack_idx > star_idx:
                return False
        
        return True if not brack_stk else False