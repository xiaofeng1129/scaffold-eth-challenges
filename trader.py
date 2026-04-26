class Trader:
    def __init__(self):
        self.positions = {}
    def open(self,symbol,price):
        print("开仓",symbol,price)
        self.positions[symbol]=price
    def close(self,symbol,price):
        print("平仓",symbol,price)
        del self.positions[symbol]
