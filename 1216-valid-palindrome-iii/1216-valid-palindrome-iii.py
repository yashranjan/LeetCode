from functools import lru_cache

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        s_len = len(s)
        len_to_fnd = len(s)-k
        dp = [0 for i in range(s_len)]
        
        for i in range(s_len-2, -1, -1):
            prev = 0
            for j in range(i+1, s_len):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j], dp[j-1])
                prev = tmp
        
        return dp[s_len-1] <= k