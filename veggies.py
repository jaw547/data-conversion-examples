vegetables = [
  {"name": "eggplant"},
  {"name": "tomato"},
  {"name": "corn"},
  {"name": "wheat"},
  {"name": "potato"},
  {"name": "kale"},
  {"name": "buckwheat"},
]

import csv

with open('veggies.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['name', 'length'])
  for veggie in vegetables:
    # I want name of vegetable
    vegetable_name = veggie['name']
    # I want the length of that word
    veggie_name_length = len(vegetable_name)
    #Write those to csv
    writer.writerow([vegetable_name, veggie_name_length])