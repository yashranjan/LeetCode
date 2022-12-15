class Solution:
    def solve(self, str1, str2, idx1, idx2, n, m):
        if idx1==n or idx2==m:
            return 0
        if (idx1, idx2) in self.cache:
            return self.cache[(idx1, idx2)]
        ans = 0
        if str1[idx1]==str2[idx2]:
            ans = 1+self.solve(str1, str2, idx1+1, idx2+1, n, m)
        else:
            ans = max(self.solve(str1, str2, idx1+1, idx2, n, m), self.solve(str1, str2, idx1, idx2+1, n, m))
        self.cache[(idx1, idx2)] = ans
        return ans
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.cache = {}
        return self.solve(text1, text2, 0, 0, len(text1), len(text2))