class StayPoint(object):
    def __init__(self, latitude, longitude, arr_time, dep_time, amount_fixes):
        self.lat = latitude
        self.long = longitude
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.amount_fixes = amount_fixes

    def __init__(self, fixes, i, j):
        self.arr_time = fixes[i].date
        self.dep_time = fixes[j].date

        lat, long = self.calculate_centroid(fixes[i:j])
        self.lat = lat
        self.long = long
        self.amount_fixes = j - i

    @staticmethod
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
        return "%f, %f, %s, %s, %d" % (self.lat, self.long, self.arr_time, self.dep_time, self.amount_fixes)

