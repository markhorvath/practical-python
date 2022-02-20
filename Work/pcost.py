# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(f)
    total_cost = 0
    for row in rows:
        try:
            total_cost += (int(row[1]) * float(row[2]))
        except ValueError:
            print(f"Value error in line: {row}.")
            continue
    f.close()
    return total_cost
    
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f"Total cost: ${cost:,.2f}.")