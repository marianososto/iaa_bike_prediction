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
