class StockSpanner:

    def __init__(self):
        self.price_stk = []

    def next(self, price: int) -> int:
        ans = 1
        while self.price_stk and self.price_stk[-1][0]<=price:
            ans+=self.price_stk.pop()[1]
        
        self.price_stk.append([price, ans])
        print(self.price_stk)
        return ans