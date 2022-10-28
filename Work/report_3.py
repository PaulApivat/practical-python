# report.py

import csv

def read_portfolio(filename):
    """
    Read a stock portfolio file into list of dictionaries with keys, name, shares & price.
    """
    portfolio = list()
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row)) #zip key-value pair of columns & rows values
            stock = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    
    return portfolio

def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices
    """
    prices = dict()
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError: # last empty line in CSV
                pass
    
    return prices


def make_report_data(portfolio, prices):
    """
    Make a list of (name, shares, prices, change) tuples,
    given a portfolio list & prices dictionary.
    
    """
    rows = list()
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

#portfolio = read_portfolio('Data/portfolio.csv')
#prices    = read_prices('Data/prices.csv')
#reportdata = make_report_data(portfolio, prices)
#print_report(reportdata)

def portfolio_report(portfoliofile, pricefile):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # create report data
    report = make_report_data(portfolio, prices)

    # print it out
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')