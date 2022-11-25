class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        stk = []
        n = len(arr)
        mod = 10**9+7
        
        for i in range(n):
            if not stk:
                stk.append(i)
            elif arr[i]<=arr[stk[-1]]:
                while len(stk) and arr[i]<=arr[stk[-1]]:
                    curr_ind = stk.pop()
                    curr = arr[curr_ind]
                    r = i
                    l = stk[-1] if len(stk) else -1
                    contri = ((r-curr_ind)*(curr_ind-l)*curr)%mod
                    ans = (ans%mod + contri%mod)%mod
                stk.append(i)
            else:
                stk.append(i)
        while len(stk):
            curr_ind = stk.pop()
            curr = arr[curr_ind]
            r = n
            l = stk[-1] if len(stk) else -1
            contri = ((r-curr_ind)*(curr_ind-l)*curr)%mod
            ans = (ans%mod + contri%mod)%mod
        
        return ans