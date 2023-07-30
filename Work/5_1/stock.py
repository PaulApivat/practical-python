
class Stock:
    """
    An instance of a stock holding, consisting of name, shares and price.
    """
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares 
        self.price = price 

    def cost(self):
        """
        return cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        sell a number of shares
        """
        self.shares -= nshares

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'


        