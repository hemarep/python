import json

f1 = open('us_states.json','r')
print(type(f1))
data = json.load(f1)


with open('us_states.json') as f:
    print(type(f))
    data = json.load(f)
    print (type(data))


for states in data:
    #print (datas['Product'])
    print (states['name'])

for state in data:
    del state['abbreviation']

with open('us_states_new.json', 'w') as fw:
    json.dump(data,fw,indent=4,sort_keys=True)
