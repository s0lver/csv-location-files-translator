class StayPoint(object):
    def __init__(self, latitude, longitude, arr_time, dep_time, amount_fixes):
        self.lat = latitude
        self.long = longitude
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.amount_fixes = amount_fixes

    @staticmethod
    def create_stay_point(fixes, i, j):
        lower_bound = i
        upper_bound = j + 1
        arr_time = fixes[i].date
        dep_time = fixes[j].date
        lat, long = StayPoint.calculate_centroid(fixes[lower_bound:upper_bound])
        amount_fixes = upper_bound - lower_bound
        return StayPoint(lat,long,arr_time,dep_time,amount_fixes)

    @classmethod
    def calculate_centroid(fixes):
        n = len(fixes)
        sum_lat, sum_long = 0, 0
        for fix in fixes:
            sum_lat += fix.latitude
            sum_long += fix.longitude

        lat = sum_lat / n
        long = sum_long / n

        return lat, long

    def __str__(self):
        return "%.9f, %.9f, %s, %s, %d" % (self.lat, self.long, self.arr_time, self.dep_time, self.amount_fixes)
