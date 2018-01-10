import json
from pprint import pprint

with open('superhero.json') as f:
    data = json.load(f)

pprint(data)