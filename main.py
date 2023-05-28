import os

import googlemaps
from datetime import datetime


def read_coordinates_csv():
    with open('codificacion_coordenadas_codificacion.csv', 'r') as f:
        lines = f.readlines()
        coordinates = []
        lines = lines[1:]  # skip header
        for line in lines:
            line = line.split(';')
            coordinates.append((line[0], line[1], line[2]))
        return coordinates


# Using gmapsClient variable , make a function which takes a list of tuples consisting of 3 values:(name of the address,the latitude,longitude), such as the one which returns the method `read_coordinates_csv`,
# and it calculates the distance between them moving on bicycle. The result should be a list of tuples consisting of 3 values:(source address,destination address, and the distance in kilometers).
# Since it calculates distances, it doesn't make sense to calculate the distance between 2 indexes more than one time, that means the distance between index i and j , is the same as the distance between j and i.
# The function should be named as `calculate_distance_bicycle`, and it should return the list of tuples.
def calculate_distance_bicycle(coordinates, gmapsClient):
    distances = []
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            source_address = coordinates[i][0]
            source_lat = coordinates[i][1]
            source_lng = coordinates[i][2]

            destination_address = coordinates[j][0]
            destination_lat = coordinates[j][1]
            destination_lng = coordinates[j][2]

            now = datetime.now()
            directions_result = gmapsClient.directions(f'{source_lat},{source_lng}',
                                                       f'{destination_lat},{destination_lng}',
                                                       mode="bicycling",
                                                       departure_time=now)
            distance = directions_result[0]['legs'][0]['distance']['value']
            distance = distance / 1000

            distances.append((source_address, destination_address, distance))

    return distances


# Make a function which takes the output of the function `calculate_distance_bicycle` and it writes it to a csv file. The function should be named as `write_csv`, and it should return nothing.
def write_csv(data):
    with open('distances.csv', 'w') as f:
        f.write('Source address;Destination address;Distance[km]\n')
        for row in data:
            f.write(f'{row[0]};{row[1]};{row[2]}\n')


google_api_key = os.getenv("GOOGLE_API_KEY")
gmapsClient = googlemaps.Client(key=google_api_key)

points_coordinates = read_coordinates_csv()
print(points_coordinates)

distances = calculate_distance_bicycle(points_coordinates, gmapsClient)
print(distances)

write_csv(distances)
