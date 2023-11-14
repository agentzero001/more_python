import json

data = []

with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)
        
tuples_list = [tuple(map(tuple, inner_list)) for inner_list in data]

