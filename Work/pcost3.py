# pcost.py

import csv

def portfolio_cost(filename):
    """
    Computes the total cost (share*price) of a portfolio file
    """
    total_cost = float()

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost

import sys 
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename: ')

cost = portfolio_cost(filename)
print('Total cost:', cost)