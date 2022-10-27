

def sumcount(n):
    """
    Returns the sum of the first n integers
    """
    total = 0
    while n > 0:
        total += n 
        n -= 1
        print(n, total)
    return total 

sumcount(100)

# Library Functions

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()

import math
x = math.sqrt(10)

# Exercises

def greeting(name):
    'Issues a greeting'
    print('Hello', name)

greeting("Paul")


# Turn Script into Function
# from pcost.py

import csv 

def portfolio_cost(filename):
    """
    compute total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1]) 
                price = float(row[2])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)

    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename: ')

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)