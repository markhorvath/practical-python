

class Stock:
    def __init__(self, sym, shares, price):
        self.name = sym
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n

