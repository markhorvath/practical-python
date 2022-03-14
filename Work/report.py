# report.py
#
# Exercise 2.4
import csv
import sys
from fileparse import parse_csv
from stock import Stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as file:
        portdicts = parse_csv(file, select=['name','shares','price'], types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return Portfolio(portfolio)

# def read_portfolio(filename):
#     if filename == None:
#         filename = 'Data/portfolio.csv'
#     with open(filename) as lines:
#         portdicts = parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
#         plist = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    
#     return plist

def read_prices(filename):
    # pdict = {}
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))
    # f = open(filename)
    # rows = csv.reader(f)
    # for row in rows:
    #     try:
    #         pdict[row[0]] = float(row[1])
    #     except Exception as e:
    #         print(e)
    #         continue
    # f.close()
    # return pdict

def make_report(portfolio, prices):
    # rows = []
    # for s in portfolio:
    #     current_price = prices[s.name]
    #     change = current_price - s.price
    #     summary = (s.name, s.shares, current_price, change)
    #     rows.append(summary)
    # return rows
    report = [(s.name, s.shares, prices[s.name], s.price - prices[s.name]) for s in portfolio]
    return report

def get_portfolio_value():
    portfolio = read_portfolio(filename)
    prices = read_prices('Data/prices.csv')
    pval = 0.0
    for s in portfolio:
        pval += s.cost()
    new_val = 0.0
    for s in portfolio:
        new_val += s.shares * prices[s.name]

    if new_val > pval:
        print(f"Portfolio valued at ${new_val:,.2f} for a gain of ${(new_val - pval):,.2f}")
    elif new_val == pval:
        print(f"Portfolio valued at ${pval:,2f} with no gain")
    else:
        print(f"Portfolio valued at ${new_val:,.2f} for a loss of -${abs(new_val - pval):,.2f}")

def print_report(reportdata, formatter):
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # print('%10s %10s %10s %10s' % headers)
    # print(('_' * 10 + ' ') * len(headers))
    # for name, shares, price, change in report:
    #     price = f"${price:0.2f}"
    #     print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
