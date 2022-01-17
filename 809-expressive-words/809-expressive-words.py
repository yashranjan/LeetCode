class Solution:
    def modifyWithFreq(self, s):
        ans = []
        n = len(s)
        i = 0
        while i < n:
            curr = s[i]
            j = i+1
            cnt  = 1
            while j < n and s[j] == s[i]:
                cnt += 1
                j += 1
            ans.extend([s[i], str(cnt)])
            i = j
        return ''.join(ans)
    
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s = self.modifyWithFreq(s)
        ans = 0
        for word in words:
            word = self.modifyWithFreq(word)
            i = j = 0
            # print(s, word)
            isMatching = True
            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    isMatching = False
                    break
                # print(s[i], word[j], end=' ')
                firstFreq = []
                secondFreq = []
                for c in s[i+1:]:
                    if not c.isdigit(): break
                    firstFreq.append(c)
                    i += 1
                for c in word[j+1:]:
                    if not c.isdigit(): break
                    secondFreq.append(c)
                    j += 1
                sFreq = int(''.join(firstFreq))
                wordFreq = int(''.join(secondFreq))
                # print(sFreq, wordFreq)
                if sFreq != wordFreq:
                    if sFreq < wordFreq or sFreq <= 2:
                        isMatchin = False
                        break
                i += 1
                j += 1
            if isMatching and i==len(s) and j==len(word):
                ans += 1
        return ans