# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv') as f:
    headers = next(f)
    total_cost = 0
    for line in f:
        line = line.split(',')
        total_cost += (int(line[1]) * float(line[2]))

print(f"Total cost: ${total_cost:,.2f}.")