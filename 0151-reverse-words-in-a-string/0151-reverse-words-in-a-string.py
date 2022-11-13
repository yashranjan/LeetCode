class Solution:
    def reverseWords(self, s: str) -> str:
        s_lst = s.strip().split(' ')
        s_lst = [i.strip() for i in s_lst if i]
        return ' '.join(reversed(s_lst))