import os
import googlemaps
from distances import read_coordinates_csv

google_api_key = os.getenv("GOOGLE_API_KEY")
gmaps_client = googlemaps.Client(key=google_api_key)

coordinates = read_coordinates_csv()
markers = "|".join([f"{lat},{lng}" for _, lat, lng in coordinates])


static_map = gmaps_client.static_map((750, 750), zoom=13, format="png32", maptype="roadmap", markers=markers)

f = open("local_map.png", 'wb')
for chunk in static_map:
    f.write(chunk)

f.close()
