import requests
from bs4 import BeautifulSoup
import json

# send a request to the website and get the HTML content
url = 'https://pokemondb.net/pokedex/all'
print(f"Sending request to {url}...") # print a message before sending the request
response = requests.get(url)
html = response.text 
print(f"Received response with status code {response.status_code}") # print a message after receiving the response

# create a soup object from the HTML content
soup = BeautifulSoup(html, 'html.parser') 

# find all the image tags in the soup object
images = soup.find_all('img') 
print(f"Found {len(images)} image tags in the HTML content") # print a message after finding the image tags

# extract the image URLs from the image tag objects
image_urls = [] # create an empty list to store the image URLs
for image in images:
    src = image.get('src') # get the src attribute of each image tag
    image_urls.append(src) # append it to the list
    print(f"Added {src} to the list of image URLs") # print a message after adding each URL to the list

import os
import requests

# create a folder called "pokemon icons" if it does not exist
if not os.path.exists("D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\pokemon icons"):
    os.mkdir("D:\\Documents\\vscode\\PokemonGoMap_SFBayArea\\pokemon icons")

# loop over all the image URLs
for url in image_urls:
    # get the file name from the URL
    file_name = url.split("/")[-1]
    # create the file path by joining the folder name and the file name
    file_path = os.path.join("pokemon icons", file_name)
    # download the image and save it to the file path
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)
