# fileparse.py
#
# Exercise 3.3
import csv
import gzip

def parse_csv(data, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    if select and not has_headers:
        raise RuntimeError("select must have headers")

    if type(data) == str:
        print("String provided as data.  Must provide lines of iterable data")
        return
    #     if data.endswith('.csv'):
    #         with open(data, 'r') as data:
    #             rows = csv.reader(data, delimiter=delimiter)
    #     elif data.endswith('.gz'):
    #         with gzip.open(data, 'rt') as data:
    #             rows = csv.reader(data, delimiter=delimiter)
    #     else:
    #         print("String provided as data but it is not a csv or gz file")
    #         return
    # else:
    rows = csv.reader(data, delimiter=delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []
    records = []
    for i, row in enumerate(rows):
        print(rows)
        try:
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
        except ValueError as e:
            if not silence_errors:
                print(f"Row {i}: Couldn't convert row {row}")
                print(f"Reason: {e}")

    return records