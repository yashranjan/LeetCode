class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        gol_val = tickets[k]
        for i in range(len(tickets)):
            if i<=k:
                ans += min(tickets[i], gol_val)
            else:
                if tickets[i] >= gol_val:
                    ans += gol_val-1
                else:
                    ans += tickets[i]
        return ans