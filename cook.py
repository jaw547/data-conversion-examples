import csv

with open('vegetables.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    print(row)

import json

with open('veggies.json', 'w') as f:
    json.dump(rows, f, indent=2)