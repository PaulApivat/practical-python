# Exercises 05_Lists

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

symlists = symbols.split(',')

for s in symlists:
    print('s =', s)

# sort
symlists.sort(reverse=True)
symlists