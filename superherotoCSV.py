import json
from pprint import pprint
import csv

# Read ur JSON file.
with open('superhero.json') as f:
	squads = json.load(f)

# Write header to CSV
with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	header = ['name', 
		'age', 
		'secretIdentity', 
		'powers', 
		'squadName', 
		'homeTown', 
		'formed', 
		'secretBase', 
		'active']
	writer.writerow(header)
	#Loop over the squads.
	for squad in squads:
		members = squad['members']

		# Loop over the members
		for member in members:
			# For each member, get thhhheeeee row.
			row = [
				member['name'],
				member['age'],
				member['secretIdentity'],
				', '.join(member['powers']),
				squad['squadName'],
				squad['homeTown'],
				squad['formed'],
				squad['secretBase'],
				squad['active']
			]
			writer.writerow(row)