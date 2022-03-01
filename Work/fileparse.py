# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            if types:
                row = [func(val) for func, val in zip(types, row) ]

            if not has_headers:
                record = tuple(row)
            else:
                record = dict(zip(headers, row))
            records.append(record)

    return records