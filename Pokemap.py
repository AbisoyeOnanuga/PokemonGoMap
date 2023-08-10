import folium # import the folium package
import folium.features
import pandas as pd # import the pandas package
import geopandas as gpd # import the geopandas package
import requests
import os 
import csv

# load the csv dataset into our python app
pokedex = "D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\PokemonSpawn_dataset\\pokemon-spawns.csv"
keys = ('name', 'longitude', 'latitude')
pokedata = []

# read the csv dataset into our python app
with open(pokedex, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pokedata.append({key: row[key] for key in keys})
print(pokedata[0])

#convert coordinate strings to float
for coords in pokedata:
    longitude = coords['longitude']
    latitude = coords['latitude']
    coords['longitude'] = float(longitude)
    coords['latitude'] = float(latitude)
print(longitude, latitude)
print(type(longitude))

#create a base map with location and zoom level
map = folium.Map(location = [37.7749, -122.4194], zoom_start=12, tiles = "CartoDB Positron", prefer_canvas = True)

#create a marker object for each pokedata
for coords in pokedata:
    coords = (coords['longitude'], coords['latitude'])
    folium.Marker(coords).add_to(map)

map.save('D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\Pokemon_map.html') # save the map as an HTML file.