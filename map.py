import folium # import the folium package
import folium.features
import pandas as pd # import the pandas package
import geopandas as gpd # import the geopandas package
import requests
import os 

# load the csv dataset into a pandas dataframe
data_file = "D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\PokemonSpawn_dataset\\pokemon-spawns.csv"
df = pd.read_csv(data_file)

# create a column in the dataframe that contains the full path to the png icons
folder_path = "D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\pokemon icons"
df["icon_path"] = df.apply(lambda row: os.path.join(folder_path, row["name"] + ".png"), axis=1)

df.dropna()

# convert the dataframe into a geodataframe
geo_data = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs='EPSG:4326')

# drop any duplicate rows from the geodataframe
geo_data = geo_data.drop_duplicates(subset=['name', 'longitude', 'latitude'], keep='first')

# create a folium map object
map = folium.Map(location=[37.7749, -122.4194], zoom_start=8, tiles="CartoDB Positron") 

# create custom icon objects for each Pokemon

# create marker objects for each Pokemon
for index, row in geo_data.iterrows():
    # create a marker for each Pokemon using the custom icon and the coordinates
    folium.Marker(location=[row["geometry"].y, row["geometry"].x], popup=f"{row['name']} ({row['num']})").add_to(map)

print(map)

map.save('D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\Pokemon_map.html') # save the map as an HTML file
