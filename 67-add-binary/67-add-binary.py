class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        a = a[::-1]
        b = b[::-1]
        i = 0
        while i<len(a) and i<len(b):
            curr = (carry+int(a[i])+int(b[i]))
            carry = curr//2
            ans += str(curr%2)
            i += 1
        while i<len(a):
            curr = (carry+int(a[i]))
            carry = curr//2
            ans += str(curr%2)    
            i += 1
        while i<len(b):
            curr = (carry+int(b[i]))
            carry = curr//2
            ans += str(curr%2)
            i += 1
        if carry:
            ans += str(carry)
        ans = ans[::-1]
        return ans
        