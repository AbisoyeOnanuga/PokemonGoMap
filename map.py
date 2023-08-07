folder_name = "pokemon icons"
folder_path = "D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\pokemon icons"
import folium # import the folium package
import pandas as pd # import the pandas package
import geopandas as gpd # import the geopandas package
import requests
import os 

map = folium.Map (location=[37.7749, -122.4194], zoom_start=12, tiles = "CartoDB Positron") # create a map object centered at San Francisco
data_file = "D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\PokemonSpawn_dataset\\pokemon-spawns.csv" # load csv file that contains pokemon sightings using pandas
folium.Marker(location = [37.7749, -122.4194],
              icon = folium.Icon(icon = "cloud", color = "red")).add_to(map)
data = pd.read_csv(data_file)
geo_data = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude), crs='EPSG:4326') # Convert the data to a geodataframe using geopandas
geo_data = geo_data.drop_duplicates(subset=['name', 'longitude', 'latitude'], keep='first') # drop duplicate rows on the longitude and latitude column

# Add several markers to the map
for index, row in data.iterrows():
  folium.Marker(location = [row["longitude"], row["latitude"]]).add_to(map)

map.save('D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\Pokemon_map.html') # save the map as an HTML file