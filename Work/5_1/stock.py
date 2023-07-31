
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
