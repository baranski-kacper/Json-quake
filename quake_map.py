import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Read file with Earthquakes in the World: last 24 file form
filename = 'data/quake.json'
with open(filename) as f:
    data_quake = json.load(f)

# Show data in better form
# readfile = 'data/read_quake.json'
# with open(readfile, 'w') as f:
#     json.dump(data_quake, f, indent=5)

# Create list with features which contain information about quakes
all_quake_dict = data_quake['features']

# var for cordinates quakes
cordinates_x, cordinates_y = [], []

for quake_dict in all_quake_dict:
    cordinate_x = quake_dict['geometry']['coordinates'][0]  # long nesting - debug helps
    cordinate_y = quake_dict['geometry']['coordinates'][1]
    cordinates_x.append(cordinate_x)
    cordinates_y.append(cordinate_y)

print(cordinates_x)
print(cordinates_y)

data = [Scattergeo(lon=cordinates_x, lat=cordinates_y)]  # Obj Scattergeo - placing points on the map
layout = Layout(title='Earthquakes in the World')

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='earthquakes.html')
