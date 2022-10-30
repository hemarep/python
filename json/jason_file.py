import json

#with open('json1.json') as f:
with open('us_states.json') as f:
    data = json.load(f)

for states in data:
    #print (datas['Product'])
    print (states['name'])

for state in data:
    del state['abbreviation']

with open('us_states_new.json', 'w') as f:
    json.dump(data,f,sort_keys=True)

