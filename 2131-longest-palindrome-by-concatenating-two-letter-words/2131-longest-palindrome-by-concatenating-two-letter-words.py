class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_cnt = Counter(words)
        
        curr_ans = 0
        central = False

        for key, value in word_cnt.items():
            if key[0]==key[1]:
                if value%2==0:
                    curr_ans += value
                else:
                    curr_ans += value-1
                    central = True
            elif key[0]<key[1] and key[1]+key[0] in word_cnt:
                curr_ans += 2*min(value, word_cnt[key[1]+key[0]])
        
        if central:
            curr_ans += 1
        return 2*curr_ans