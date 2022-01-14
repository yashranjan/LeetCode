class Solution:
    def myAtoi(self, s: str) -> int:
        intMin, intMax = -2**31, 2**31-1
        ind = ans = 0
        negation = 1
        n = len(s)
        while ind < n and s[ind] == ' ':
            ind += 1
        if ind < n and s[ind] == '-':
            negation = -1
            ind += 1
        elif ind < n and s[ind] == '+':
            negation = 1
            ind += 1
        while ind < n and s[ind].isdigit():
            currDigit = ord(s[ind])-ord('0')
            if (ans > intMax//10) or (ans == intMax//10 and currDigit > intMax%10):
                return intMax if negation == 1 else intMin
            ans = (ans*10)+currDigit
            ind += 1
        return negation*ans