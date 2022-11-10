class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)<=1:
            return s
        str_lst = list(s)
        curr_idx = 0
        next_idx = 1
        lst_len = len(str_lst)
        left_pos = []
        while next_idx<lst_len:
            # print(curr_idx, next_idx)
            if str_lst[curr_idx]=='':
                curr_idx+=1
                if curr_idx==next_idx:
                    next_idx+=1
                else:
                    continue
            if str_lst[curr_idx]==str_lst[next_idx]:
                str_lst[curr_idx] = str_lst[next_idx] = ''
                curr_idx = -1 if not left_pos else left_pos.pop()
                next_idx += 1
                if curr_idx == -1:
                    curr_idx=next_idx
                    next_idx=next_idx+1
            else:
                left_pos.append(curr_idx)
                curr_idx, next_idx = curr_idx+1, next_idx+1
            # print(str_lst)

        return ''.join(str_lst)
        