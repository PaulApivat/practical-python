# report.py
#
# Exercise 2.4
import csv

# tuple version
def read_portfolio(filename):
    """
    Puts name, shares, price into a list of tuples
    """
    portfolio = list()
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    
    return portfolio

# dictionary version
def read_portfolio_2(filename):
    """
    Puts name, shares, price into a list of dictionaries
    """
    portfolio = list()
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
    
    return portfolio


# read stock prices 
def read_prices(filename):
    """
    read file with two colunns, string, float into a list of dictionaries
    """
    stocks = list()
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                holding = {'name': row[0], 'price': float(row[1])}
                stocks.append(holding)
            except IndexError:
                pass
        

    return stocks

portfolio = read_portfolio_2('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')


