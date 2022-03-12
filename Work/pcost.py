# pcost.py
#
# Exercise 1.27
import csv
import sys
from report import read_portfolio
from stock import Stock


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    cost = sum([s.cost() for s in portfolio])
    print(f"Total cost: ${cost:,.2f}.")
    return cost
    # f = open(filename)
    # rows = csv.reader(f)
    # headers = next(rows)
    # print(headers)
    # total_cost = 0
    # for rowno, row in enumerate(rows, start=1):
    #     record = dict(zip(headers, row))
    #     print(record)
    #     try:
    #         nshares = int(record['shares'])
    #         price = float(record['price'])
    #         total_cost += nshares * price
    #     # This catches errors in int() and float() conversions above
    #     except ValueError:
    #         print(f'Row {rowno}: Bad row: {row}')
    #         continue
    # f.close()
    # return total_cost
    
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

# cost = portfolio_cost(filename)
# print(type(cost))
# print(f"Total cost: ${cost[0]:,.2f}.")

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile' % args[0])
    portfolio_cost(args[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)