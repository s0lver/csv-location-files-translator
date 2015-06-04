from entities import BatteryStatus
import math


def time_diff(pi, pj):
    diff = pj.date - pi.date
    return math.fabs(diff.total_seconds())


def distance_diff(pi, pj):
    lat1, lon1 = pi.latitude, pi.longitude
    lat2, lon2 = pj.latitude, pj.longitude

    max_iter = 20

    lat1 *= math.pi / 180
    lat2 *= math.pi / 180
    lon1 *= math.pi / 180
    lon2 *= math.pi / 180

    a = 6378137.0
    b = 6356752.3142
    f = (a - b) / a
    asq_minus_bsq_over_bsq = (a * a - b * b) / (b * b)

    l = lon2 - lon1
    A = 0.0
    u1 = math.atan((1.0 - f) * math.tan(lat1))
    u2 = math.atan((1.0 - f) * math.tan(lat2))

    cos_u1 = math.cos(u1)
    cos_u2 = math.cos(u2)
    sin_u1 = math.sin(u1)
    sin_u2 = math.sin(u2)
    cos_u1_cos_u2 = cos_u1 * cos_u2
    sin_u1_sin_u2 = sin_u1 * sin_u2

    sigma = 0.0
    delta_sigma = 0.0

    the_lambda = l
    for i in range(0, max_iter):
        lambda_orig = the_lambda
        cos_lambda = math.cos(the_lambda)
        sin_lambda = math.sin(the_lambda)
        t1 = cos_u2 * sin_lambda
        t2 = cos_u1 * sin_u2 - sin_u1 * cos_u2 * cos_lambda
        sin_sq_lambda = t1 * t1 + t2 * t2
        sin_sigma = math.sqrt(sin_sq_lambda)
        cos_sigma = sin_u1_sin_u2 + cos_u1_cos_u2 * cos_lambda
        sigma = math.atan2(sin_sigma, cos_sigma)
        sin_alpha = 0.0 if sin_sigma == 0 else cos_u1_cos_u2 * sin_lambda / sin_sigma

        cos_sq_alpha = 1.0 - sin_alpha * sin_alpha
        cos2_sm = 0.0 if cos_sq_alpha == 0 else cos_sigma - 2.0 * sin_u1_sin_u2 / cos_sq_alpha

        u_squared = cos_sq_alpha * asq_minus_bsq_over_bsq
        A = 1 + (u_squared / 16384.0) * (4096.0 + u_squared * (-768 + u_squared * (320.0 - 175.0 * u_squared)))

        B = (u_squared / 1024.0) * (256.0 + u_squared * (-128.0 + u_squared * (74.0 - 47.0 * u_squared)))

        C = (f / 16.0) * cos_sq_alpha * (4.0 + f * (4.0 - 3.0 * cos_sq_alpha))

        cos2_sm_sq = cos2_sm * cos2_sm

        delta_sigma = B * sin_sigma * \
                      (cos2_sm + (B / 4.0) * \
                       (cos_sigma * (-1.0 + 2.0 * cos2_sm_sq) - \
                        (B / 6.0) * cos2_sm * (-3.0 + 4.0 * sin_sigma * sin_sigma) * (-3.0 + 4.0 * cos2_sm_sq)))

        the_lambda = l + (1.0 - C) * f * sin_alpha * \
                         (sigma + C * sin_sigma * (cos2_sm + C * cos_sigma * (-1.0 + 2.0 * cos2_sm * cos2_sm)))

        delta = (the_lambda - lambda_orig) / the_lambda
        if math.fabs(delta) < 1.0e-12:
            break

    distance = b * A * (sigma - delta_sigma)
    return distance


class GpsFix(object):
    def __init__(self, id, id_trajectory, obtained, latitude, longitude, altitude, accuracy, speed, date,
                 level, voltage, status, temperature, connected):
        self.id = id
        self.id_trajectory = id_trajectory
        self.obtained = obtained
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.accuracy = accuracy
        self.speed = speed
        self.date = date
        self.batteryInfo = BatteryStatus.BatteryStatus(level, voltage, status, temperature, connected)

    def __str__(self):
        return '%d, %d, %i, %f, %f, %f, %s, %s' % \
               (self.id, self.id_trajectory, self.obtained, self.latitude, self.longitude, self.accuracy,
                self.date, self.batteryInfo)
