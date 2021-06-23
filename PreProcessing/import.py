import json, sys

with open('listKick0.json', 'r') as fp:
	data = json.load(fp)

print(sys.getsizeof(data[0]), len(data))