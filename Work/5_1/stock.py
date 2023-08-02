
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


# How inheritance works

# Reading Attributes with Single Inheritance
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass

print(B.__bases__)

# Method Reolution Order or MRO

print(E.__mro__)

# MRO in Multiple Inheritance

class F: pass 
class G: pass 
class H(F, G): pass 
class I(G): pass 
class J(H, I): pass

print(H.__mro__)
print(I.__mro__)

# MIXIN Pattern

class Loud:
    def noise(self):
        return super().noise().upper()

print(Loud.__mro__)
print(Loud.__bases__)


# Exercises 5.1 - 5.5
from stock import Stock 

goog = Stock('GOOG',100,490.10)
ibm  = Stock('IBM',50, 91.23)

print(goog.__dict__)
print(ibm.__dict__)

goog.date = '6/11/2007'
print(goog.__dict__)

goog.__dict__['time'] = '9:45am'
print(goog.time)

print(goog.cost())
print(ibm.cost())

print(Stock.__dict__['cost'](goog))
print(Stock.__dict__['cost'](ibm))