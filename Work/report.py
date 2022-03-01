# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    if filename == None:
        filename = 'Data/portfolio.csv'
    plist = []
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for i, row in enumerate(rows):
        record = dict(zip(headers, row))
        stock = {
            'name'   : record['name'],
            'shares' : int(record['shares']),
            'price'   : float(record['price'])
        }
        try:
            plist.append(stock)
        except Exception as e:
            print(f"Error in line {i}")
    f.close()
    print(plist)
    return plist

def read_prices(filename):
    pdict = {}
    f = open(filename)
    rows = csv.reader(f)
    for row in rows:
        try:
            pdict[row[0]] = float(row[1])
        except Exception as e:
            print(e)
            continue
    f.close()
    return pdict

def make_report(portfolio, prices):
    report = [(el['name'], int(el['shares']), float(prices[el['name']]), (int(el['shares']) * float(el['price'])) - (int(el['shares']) * float(prices[el['name']]))) for el in portfolio]
    return report

def get_portfolio_value():
    portfolio = read_portfolio(filename)
    prices = read_prices('Data/prices.csv')
    pval = 0.0
    for el in portfolio:
        pval += el['shares'] * el['price']
    new_val = 0.0
    for el in portfolio:
        new_val += el['shares'] * prices[el['name']]

    if new_val > pval:
        print(f"Portfolio valued at ${new_val:,.2f} for a gain of ${(new_val - pval):,.2f}")
    elif new_val == pval:
        print(f"Portfolio valued at ${pval:,2f} with no gain")
    else:
        print(f"Portfolio valued at ${new_val:,.2f} for a loss of -${abs(new_val - pval):,.2f}")

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('_' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        price = f"${price:0.2f}"
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
    # for row in report:
    #     print('%10s %10d %10.2f %10.2f' % row)

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'
def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')