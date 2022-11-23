class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirror = ['0', '1', '-1', '-1', '-1', '-1', '9', '-1', '8', '6']
        
        new_str = ''.join([mirror[ord(i)-ord('0')] for i in reversed(num)])

        return new_str == num