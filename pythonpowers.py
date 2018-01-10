import json
from pprint import pprint
#Read JSON
with open('superhero.json') as f:
    data = json.load(f)

#Create a blank list of powers
allPowers=[]

#Loop over members
members = data['members']
for member in members:
	#for each member, loop over powers
	powers = member['powers']
	for power in powers:
		#add that to our list of powers
		allPowers.append(power)

#get only unique elements
uniquePowers = list(set(allPowers))

pprint(uniquePowers)