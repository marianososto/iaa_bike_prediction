from cyclist_variance import CyclistVariance
from definitions import DistanceSourceDestination, CyclistsMeasure


def read_measure_points() -> list[CyclistsMeasure]:
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


def read_distances_csv() -> list[DistanceSourceDestination]:
    with open('distances.csv', 'r') as f:
        lines = f.readlines()
        result = []
        lines = lines[1:]  # skip header
        for line in lines:
            line = line.replace('\n', '')
            line = line.split(';')
            result.append((DistanceSourceDestination(line[0], line[1], line[2])))
        return result


def same_year(_m1, _m2: CyclistsMeasure) -> bool:
    return _m1.year == _m2.year


def same_month(_m1, _m2: CyclistsMeasure) -> bool:
    return _m1.month == _m2.month


def create_pairs_with_distance(_measures, _distances_src_dest) -> list[
    (CyclistsMeasure, CyclistsMeasure, DistanceSourceDestination)]:
    result = []
    for m1 in _measures:
        for m2 in _measures.copy():
            if same_year(m1, m2) and same_month(m1, m2) and m1.crossing_point != m2.crossing_point:
                for d in _distances_src_dest:
                    if (d.source == m1.crossing_point and d.destination == m2.crossing_point) or (
                            d.source == m2.crossing_point and d.destination == m1.crossing_point):
                        result.append((m1, m2, d))
    return result


def write_cyclist_variance() -> None:
    with open('cyclist_variance.csv', 'w') as f:
        f.write(
            'Origen,Destino,Distancia[km],Año,Mes,Diferencia de ciclistas,Calle 1 origen,Calle 2 origen,Calle 1 origen id,Calle 2 origen id,Calle 1 destino,Calle 2 destino,Calle 1 destino id,Calle 2 destino id\n')
        for c in cyclist_variance:
            f.write(
                f'{c.source},{c.destination},{c.distance},{c.year},{c.month},{c.cyclist_diff},{c.src_street_1},{c.src_street_2},{c.src_street_1_id},{c.src_street_2_id},{c.dst_street_1},{c.dst_street_2},{c.dst_street_1_id},{c.dst_street_2_id}\n')


distances_src_dest = read_distances_csv()
measures = read_measure_points()
measures_1 = measures.copy()

pairs_with_distances = create_pairs_with_distance(measures_1, distances_src_dest)

cyclist_variance = []
for (src, dst, d) in pairs_with_distances:
    cyclist_variance.append(
        CyclistVariance(src.crossing_point,
                        dst.crossing_point,
                        d.distance,
                        src.year,
                        src.month,
                        int(src.cyclist_count) - int(dst.cyclist_count),
                        src.street_1,
                        src.street_2,
                        src.street_1_id,
                        src.street_2_id,
                        dst.street_1,
                        dst.street_2,
                        dst.street_1_id,
                        dst.street_2_id))

write_cyclist_variance()
