# año,mes,punto_cruce,cantidad_ciclistas,Calle 1,Calle 2,Calle 1 Id,Calle 2 Id,Mes Id

def read_measure_points():
    with open('volumen-ciclistas-mensuales.csv', 'r') as f:
        lines = f.readlines()
        result = []
        lines = lines[1:]  # skip header
        for line in lines:
            line = line.replace('\n', '')
            line = line.split(',')
            result.append(
                (CyclistsMeasure(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])))
        return result


class CyclistsMeasure:
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
    def __init__(self, source, destination, dist, street_1, street_2, street_1_id, street_2_id):
        self.source = source
        self.destination = destination
        self.distance = dist
        self.street_1 = street_1
        self.street_2 = street_2
        self.street_1_id = street_1_id
        self.street_2_id = street_2_id


def same_year(_m1, _m2: CyclistsMeasure):
    return _m1.year == _m2.year


def same_month(_m1, _m2: CyclistsMeasure):
    return _m1.month == _m2.month


def calculate_distances(_measures, _distances_src_dest) -> list[
    (CyclistsMeasure, CyclistsMeasure, DistanceSourceDestination)]:
    result = []
    for m1 in _measures:
        for m2 in _measures.copy():
            if same_year(m1, m2) and same_month(m1, m2) and m1.crossing_point != m2.crossing_point:
                for d in _distances_src_dest:
                    if d.source == m1.crossing_point and d.destination == m2.crossing_point:
                        result.append((m1, m2, d))
    return result


class CyclistVariance:
    def __init__(self,
                 source,
                 destination,
                 dist,
                 year,
                 month,
                 cyclist_diff,
                 src_street_1,
                 src_street_2,
                 src_street_1_id,
                 src_street_2_id,
                 dst_street_1,
                 dst_street_2,
                 dst_street_1_id,
                 dst_street_2_id):
        self.source = source
        self.destination = destination
        self.distance = dist
        self.year = year
        self.month = month
        self.cyclist_diff = cyclist_diff
        self.src_street_1 = src_street_1
        self.src_street_2 = src_street_2
        self.src_street_1_id = src_street_1_id
        self.src_street_2_id = src_street_2_id
        self.dst_street_1 = dst_street_1
        self.dst_street_2 = dst_street_2
        self.dst_street_1_id = dst_street_1_id
        self.dst_street_2_id = dst_street_2_id


def write_cyclist_variance():
    with open('cyclist_variance.csv', 'w') as f:
        f.write(
            'Origen,Destino,Distancia[km],Año,Mes,Diferencia de ciclistas,Calle 1 origen,Calle 2 origen,Calle 1 origen id,Calle 2 origen id,Calle 1 destino,Calle 2 destino,Calle 1 destino id,Calle 2 destino id\n')
        for c in cyclist_variance:
            f.write(
                f'{c.source},{c.destination},{c.distance},{c.year},{c.month},{c.cyclist_diff},{c.src_street_1},{c.src_street_2},{c.src_street_1_id},{c.src_street_2_id},{c.dst_street_1},{c.dst_street_2},{c.dst_street_1_id},{c.dst_street_2_id}\n')


distances_src_dest = read_distances_source_destination()
measures = read_measure_points()
measures_1 = measures.copy()

distances = calculate_distances(measures_1, distances_src_dest)
# Iterate distances and calculate the difference between the cyclist count and save it a new list of CyclistVariance
cyclist_variance = []
for d in distances:
    cyclist_variance.append(
        CyclistVariance(d[0].crossing_point,
                        d[1].crossing_point,
                        d[2].distance,
                        d[0].year,
                        d[0].month,
                        int(d[0].cyclist_count) - int(d[1].cyclist_count),
                        d[0].street_1,
                        d[0].street_2,
                        d[0].street_1_id,
                        d[0].street_2_id,
                        d[1].street_1,
                        d[1].street_2,
                        d[1].street_1_id,
                        d[1].street_2_id))

write_cyclist_variance()
