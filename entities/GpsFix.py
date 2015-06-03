from entities import BatteryStatus
from datetime import datetime
import math

def time_diff(pi, pj):
    diff = pj.date - pi.date
    return math.fabs(diff.total_seconds())

def distance_diff(pi, pj):
    lat1 = pi.latitude
    lon1 = pi.longitude
    lat2 = pj.latitude
    lon2 = pj.longitude

    results = []                                            # float[] results = new float[2];
    MAXITERS = 20                                           # int MAXITERS = 20;
                                                            #
    lat1 *= math.pi / 180                                   # lat1 *= Math.PI / 180.0;
    lat2 *= math.pi / 180                                   # lat2 *= Math.PI / 180.0;
    lon1 *= math.pi / 180                                   # lon1 *= Math.PI / 180.0;
    lon2 *= math.pi / 180                                   # lon2 *= Math.PI / 180.0;
                                                            #
    a = 6378137.0                                           # double a = 6378137.0; // WGS84 major axis
    b = 6356752.3142                                        # double b = 6356752.3142; // WGS84 semi-major axis
    f = (a - b) / a                                         # double f = (a - b) / a;
    aSqMinusBSqOverBSq = (a * a - b * b) / (b * b)          # double aSqMinusBSqOverBSq = (a * a - b * b) / (b * b);
                                                            #
    L = lon2 - lon1;                                        # double L = lon2 - lon1;
    A = 0.0                                                 # double A = 0.0;
    U1 = math.atan((1.0 - f) * math.tan(lat1))              # double U1 = Math.atan((1.0 - f) * Math.tan(lat1));
    U2 = math.atan((1.0 - f) * math.tan(lat2));             # double U2 = Math.atan((1.0 - f) * Math.tan(lat2));
                                                            #
    cosU1 = math.cos(U1)                                    # double cosU1 = Math.cos(U1);
    cosU2 = math.cos(U2)                                    # double cosU2 = Math.cos(U2);
    sinU1 = math.sin(U1)                                    # double sinU1 = Math.sin(U1);
    sinU2 = math.sin(U2)                                    # double sinU2 = Math.sin(U2);
    cosU1cosU2 = cosU1 * cosU2                              # double cosU1cosU2 = cosU1 * cosU2;
    sinU1sinU2 = sinU1 * sinU2                              # double sinU1sinU2 = sinU1 * sinU2;
                                                            #
    sigma = 0.0                                             # double sigma = 0.0;
    deltaSigma = 0.0                                        # double deltaSigma = 0.0;
    cosSqAlpha = 0.0                                        # double cosSqAlpha = 0.0;
    cos2SM = 0.0                                            # double cos2SM = 0.0;
    cosSigma = 0.0                                          # double cosSigma = 0.0;
    sinSigma = 0.0                                          # double sinSigma = 0.0;
    cosLambda = 0.0                                         # double cosLambda = 0.0;
    sinLambda = 0.0                                         # double sinLambda = 0.0;
                                                            #
    LAMBDA = L                                              # double lambda = L; // initial guess
    for iter in range(0,MAXITERS):                          # for (int iter = 0; iter < MAXITERS; iter++){
        lambdaOrig = LAMBDA                                 #     double lambdaOrig = lambda;
        cosLambda = math.cos(LAMBDA)                        #     cosLambda = Math.cos(lambda);
        sinLambda = math.sin(LAMBDA)                        #     sinLambda = Math.sin(lambda);
        t1 = cosU2 * sinLambda                              #     double t1 = cosU2 * sinLambda;
        t2 = cosU1 * sinU2 - sinU1 * cosU2 * cosLambda      #     double t2 = cosU1 * sinU2 - sinU1 * cosU2 * cosLambda;
        sinSqSigma = t1 * t1 + t2 * t2                      #     double sinSqSigma = t1 * t1 + t2 * t2; // (14)
        sinSigma = math.sqrt(sinSqSigma)                    #     sinSigma = Math.sqrt(sinSqSigma);
        cosSigma = sinU1sinU2 + cosU1cosU2 * cosLambda      #     cosSigma = sinU1sinU2 + cosU1cosU2 * cosLambda; // (15)
        sigma = math.atan2(sinSigma, cosSigma)              #     sigma = Math.atan2(sinSigma, cosSigma); // (16)
        sinAlpha = 0.0 if sinSigma == 0 else cosU1cosU2 * sinLambda / sinSigma      #     double sinAlpha = (sinSigma == 0) ? 0.0 :
                                                            #             cosU1cosU2 * sinLambda / sinSigma; // (17)
        cosSqAlpha = 1.0 - sinAlpha * sinAlpha              #     cosSqAlpha = 1.0 - sinAlpha * sinAlpha;
        cos2SM = 0.0 if cosSqAlpha == 0 else cosSigma - 2.0 * sinU1sinU2 / cosSqAlpha#     cos2SM = (cosSqAlpha == 0) ? 0.0 :
                                                            #             cosSigma - 2.0 * sinU1sinU2 / cosSqAlpha; // (18)
                                                            #
        uSquared = cosSqAlpha * aSqMinusBSqOverBSq          #     double uSquared = cosSqAlpha * aSqMinusBSqOverBSq; // defn
        A = 1 + (uSquared / 16384.0) * (4096.0 + uSquared * (-768 + uSquared * (320.0 - 175.0 * uSquared)))

        #     A = 1 + (uSquared / 16384.0) * // (3)
        #             (4096.0 + uSquared *
        #                     (-768 + uSquared * (320.0 - 175.0 * uSquared)));

        B = (uSquared / 1024.0) * (256.0 + uSquared * (-128.0 + uSquared * (74.0 - 47.0 * uSquared)))

        #     double B = (uSquared / 1024.0) * // (4)
        #             (256.0 + uSquared *
        #                     (-128.0 + uSquared * (74.0 - 47.0 * uSquared)));

        C = (f / 16.0) * cosSqAlpha *(4.0 + f * (4.0 - 3.0 * cosSqAlpha))
        #     double C = (f / 16.0) *
        #             cosSqAlpha *
        #             (4.0 + f * (4.0 - 3.0 * cosSqAlpha)); // (10)

        cos2SMSq = cos2SM * cos2SM                          #     double cos2SMSq = cos2SM * cos2SM;

        deltaSigma = B * sinSigma * \
            (cos2SM + (B / 4.0) * \
            (cosSigma * (-1.0 + 2.0 * cos2SMSq) - \
             (B / 6.0) * cos2SM * (-3.0 + 4.0 * sinSigma * sinSigma) *(-3.0 + 4.0 * cos2SMSq)))
        #     deltaSigma = B * sinSigma * // (6)
        #             (cos2SM + (B / 4.0) *
        #                     (cosSigma * (-1.0 + 2.0 * cos2SMSq) -
        #                             (B / 6.0) * cos2SM *
        #                                     (-3.0 + 4.0 * sinSigma * sinSigma) *
        #                                     (-3.0 + 4.0 * cos2SMSq)));
        #


        LAMBDA = L + (1.0 - C) * f * sinAlpha * \
                     (sigma + C * sinSigma * (cos2SM + C * cosSigma * (-1.0 + 2.0 * cos2SM * cos2SM)))
        #     lambda = L +
        #             (1.0 - C) * f * sinAlpha *
        #                     (sigma + C * sinSigma *
        #                             (cos2SM + C * cosSigma *
        #                                     (-1.0 + 2.0 * cos2SM * cos2SM))); // (11)
        #

        delta = (LAMBDA - lambdaOrig) / LAMBDA              #     double delta = (lambda - lambdaOrig) / lambda;
        if math.fabs(delta) < 1.0e-12:                       #     if (Math.abs(delta) < 1.0e-12) {
            break                                           #         break;
                                                            #     }
                                                            # }
                                                            #
    distance = (float) (b * A * (sigma - deltaSigma))   # float distance = (float) (b * A * (sigma - deltaSigma));
    return distance                                     # results[0] = distance;


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

