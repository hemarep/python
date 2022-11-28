import json
import ssl
from urllib.request import urlopen

# This restores the same behavior as before --- New code to bypass API SSL

context = ssl._create_unverified_context()
with urlopen("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json", context=context) as f:
    #print(type(f))
    source = f.read()

#with urlopen('https://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json') as response:
#    source = response.read()

data = json.loads(source)
#print(json.dumps(data,indent=4))

#print(type(data))
# print(json.dumps(data,indent=4))
# print("-------------------------------------------------")
#print(json.dumps(data['dataseries'],indent=4))
dataseries_l = list()
dataseries_d = dict()

for item in data['dataseries']:

    # dataseries_d['timepoint_abc'] = "item['timepoint']"
    # dataseries_d['timepoint_abc'] = "item['timepoint']"
    # dataseries_d['seeing_abc'] = "item['seeing']"
    # dataseries_d['transparency_abc'] = "item['transparency']"
    # dataseries_d['rh2m_abc'] = "item['rh2m']"
    # dataseries_d['lifted_index_abc'] = "item['lifted_index']"

    dataseries_l.append({
        'timepoint_abc': item['timepoint'],
        'cloudcover_abc': item['cloudcover'],
        'seeing_abc': item['seeing'],
        'transparency_abc': item['transparency'],
        'rh2m_abc': item['rh2m'],
        'lifted_index_abc': item['lifted_index']
    })


with open('Weather_forecasts.json', 'w') as f:
    json.dump(dataseries_l, f, indent=2)

print(dataseries_d)