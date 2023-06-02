# año,mes,punto_cruce,cantidad_ciclistas,Calle 1,Calle 2,Calle 1 Id,Calle 2 Id,Mes Id

def read_cyclist_measures():
    with open('volumen-ciclistas-mensuales.csv', 'r') as f:
        lines = f.readlines()
        result = []
        lines = lines[1:]  # skip header
        for line in lines:
            line = line.replace('\n', '')
            line = line.split(',')
            result.append((Measure(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])))
        return result


class Measure:
    def __init__(self, year, month, crossing_point, cyclist_count, street_1, street_2, street_1_id, street_2_id,
                 month_id):
        self.year = year
        self.month = month
        self.crossing_point = crossing_point
        self.cyclist_count = cyclist_count
        self.street_1 = street_1
        self.street_2 = street_2
        self.street_1_id = street_1_id
        self.street_2_id = street_2_id
        self.month_id = month_id


def read_distances_source_destination():
    with open('distancias_origen_destino.csv', 'r') as f:
        lines = f.readlines()
        result = []
        lines = lines[1:]  # skip header
        for line in lines:
            line = line.replace('\n', '')
            line = line.split(',')
            result.append((DistanceSourceDestination(line[0], line[1], line[2], line[3], line[4], line[5], line[6])))
        return result


# Origen,Destino,Distancia[km],Calle 1,Calle 2,Calle 1 id,Calle 2 id
class DistanceSourceDestination:
    def __init__(self, source, destination, distance, street_1, street_2, street_1_id, street_2_id):
        self.source = source
        self.destination = destination
        self.distance = distance
        self.street_1 = street_1
        self.street_2 = street_2
        self.street_1_id = street_1_id
        self.street_2_id = street_2_id


distances_src_dest = read_distances_source_destination()
#print(distances_src_dest)
