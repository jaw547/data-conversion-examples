import csv

with open('manNothot2.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

for row in rows:
    print(row)