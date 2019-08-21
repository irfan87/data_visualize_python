import os
import json

filename = os.path.abspath('downloading_data/json_data/data/eq_1_day_m1.json')

with open(filename) as json_file:
    all_eq_data = json.load(json_file)

readable_file = os.path.abspath('downloading_data/json_data/data/readable_eq_data.json')

with open(readable_file, 'w') as json_readable_file:
    json.dump(all_eq_data, json_readable_file, indent=4)

all_eq_dicts = all_eq_data['features']

mags = []
lons = []
lats = []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:5])
print(lons[:5])
print(lats[:5])