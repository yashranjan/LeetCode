class Solution:
    def reverseVowels(self, s: str) -> str:
        left_ptr, right_ptr = 0, len(s)-1
        vowels_list = ['a', 'e', 'i', 'o', 'u']
        while left_ptr<right_ptr:
            while left_ptr<right_ptr and s[left_ptr].lower() not in vowels_list:
                left_ptr+=1
            while left_ptr<right_ptr and s[right_ptr].lower() not in vowels_list:
                right_ptr-=1
            if left_ptr>=right_ptr:
                break
            s = s[:left_ptr]+s[right_ptr]+s[left_ptr+1:right_ptr]+s[left_ptr]+s[right_ptr+1:]
            left_ptr+=1
            right_ptr-=1
        return s
            