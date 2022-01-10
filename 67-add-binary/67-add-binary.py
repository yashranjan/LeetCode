class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, ans, i, j = 0, [], len(a)-1, len(b)-1
        while i>=0 or j>=0 or carry:
            carry += int(a[i]) if i>=0 else 0
            carry += int(b[j]) if j>=0 else 0
            ans += str(carry%2)
            carry //= 2
            i, j = i-1, j-1
        ans = ans[::-1]
        return ''.join(ans)
        