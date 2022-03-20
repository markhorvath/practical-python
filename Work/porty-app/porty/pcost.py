# pcost.py
#
# Exercise 1.27
import csv
import sys
from . import report
from . import stock
from .stock import Stock


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
    # print(f"Total cost: ${cost:,.2f}.")

    
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