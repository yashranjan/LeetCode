class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        idx = -1
        try:
            idx = num_str.index('6')
        except ValueError as ve:
            idx = -1
        if idx!=-1:
            num_str = num_str[:idx] + '9' + num_str[idx+1:]
        return int(num_str)