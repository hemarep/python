import json
import ssl

from urllib.request import urlopen

# This restores the same behavior as before.
context = ssl._create_unverified_context()
with urlopen("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json", context=context) as response:
    source = response.read()

#with urlopen('http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json') as response:
#    source = response.read()

data = json.loads(source)
####print(json.dumps(data, indent=2))

print(type(data))
# print(json.dumps(data,indent=4))
# print("-------------------------------------------------")
# print(json.dumps(data['dataseries'],indent=4))
dataseries_l = list()
dataseries_l = dict()

for item in data['dataseries']:
    dataseries_l['timepoint'] = item['timepoint']
    dataseries_l['timepoint'] = item['timepoint']
    dataseries_l['seeing'] = item['seeing']
    dataseries_l['transparency'] = item['transparency']
    dataseries_l['rh2m'] = item['rh2m']
    dataseries_l['lifted_index'] = item['lifted_index']

    dataseries_l.update({
        'timepoint': item['timepoint'],
        'cloudcover': item['cloudcover'],
        'seeing': item['seeing'],
        'transparency': item['transparency'],
        'rh2m': item['rh2m'],
        'lifted_index': item['lifted_index']
    })

with open('Weather_forecasts.json', 'w') as f:
    json.dump(dataseries_l, f, indent=2)
