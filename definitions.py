class DistanceSourceDestination:
    def __init__(self, source, destination, dist):
        self.source = source
        self.destination = destination
        self.distance = dist


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
