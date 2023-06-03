from distance_source_destination import DistanceSourceDestination




# Given a list[DistanceSourceDestination] , duplicate all the distances in the opposite direction

def write_distances_source_destination(dsts: list[DistanceSourceDestination]):
    with open('distancias_origen_destino.csv', 'w') as f:
        f.write(
            'Origen,Destino,Distancia[km],Calle 1 orig,Calle 2 orig,Calle 1 id orig,Calle 2 id orig,Calle 1 dest,Calle 2 dest,Calle 1 id dest,Calle 2 id dest\n')
        for distance in dsts:
            f.write(
                f'{distance.source},{distance.destination},{distance.distance},{distance.src_street_1},{distance.src_street_2},{distance.src_street_1_id},{distance.src_street_2_id},{distance.dst_street_1},{distance.dst_street_2},{distance.dst_street_1_id},{distance.dst_street_2_id}\n')


#distances = read_distances_source_destination()
#write_distances_source_destination(distances)
