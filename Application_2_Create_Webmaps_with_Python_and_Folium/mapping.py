# This code creates a layered map that contains points describing events in my life. 
# The original example was mapping volcanoes on the map of the US. 
import folium
import pandas as pd 

# Setting up my lists that will pass through my for statement below
data = pd.read_csv("mylife.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
info = list(data['STATEMENT'])
stage = list(data['LIFEPERIOD'])

# This function is what determines the color of the marker on the map according to the relation to my life
def color_the_markers(period_of_life):
    if period_of_life == 'Childhood':
        return 'green'
    elif period_of_life == 'With Brian':
        return 'red'
    elif period_of_life == 'Education':
        return 'blue'
    else:
        return 'pink'

# Setting up the original map
map = folium.Map(location = [40.400963, -82.811120],tiles="Mapbox Bright")

# Setting up feature groups to be used with layer control on the map. Each feature can be turned on or off
feat_group_locations = folium.FeatureGroup(name="Key Locations")
feat_group_states = folium.FeatureGroup(name="State Outlines")

# Adding the state outlines map with GeoJson
feat_group_states.add_child(folium.GeoJson(data=(open('gz_2010_us_040_00_500k.json','r').read())))

# Determining marker location, message, and color 
for lati, longi, words, period in zip(lat, lon, info, stage):
    feat_group_locations.add_child(folium.Marker(location=[lati, longi], popup=words,
    icon= folium.Icon(color=color_the_markers(period))))

# Adding all of the final features to the map
map.add_child(feat_group_locations)
map.add_child(feat_group_states)
map.add_child(folium.LayerControl())

# Save the map to an html file
map.save("Map1.html")
 
