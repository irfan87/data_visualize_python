import os
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = os.path.abspath('downloading_data/json_data/data/eq_data_30_day_m1.json')

with open(filename) as json_file:
    all_eq_data = json.load(json_file)

readable_file = os.path.abspath('downloading_data/json_data/data/readable_eq_data_30_days.json')

with open(readable_file, 'w') as json_readable_file:
    json.dump(all_eq_data, json_readable_file, indent=4)

all_eq_dicts = all_eq_data['features']

mags = []
lons = []
lats = []
hover_text = []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

# map the eathquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {
            'title': 'Magnitude'
        }
    }
}]

eq_data_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': eq_data_layout}
save_filename = os.path.abspath('downloading_data/json_data/eq_results/global_earthquakes_30_days.html')
offline.plot(fig, filename=save_filename)