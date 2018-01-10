#Import ur modules.
import csv
import json

#Read a csv and turn it into JSON dict.
with open('vegetables.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

#Write to JSON file.
with open('veggies.json', 'w') as f:
    json.dump(rows, f, indent=2)