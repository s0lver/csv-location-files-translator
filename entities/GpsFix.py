from entities import BatteryStatus


class GpsFix(object):
    def __init__(self, id, id_trajectory, obtained, latitude, longitude, altitude, accuracy, speed, date,
                 level, voltage, status, temperature, connected):
        self._id = id
        self._id_trajectory = id_trajectory
        self._obtained = obtained
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude
        self._accuracy = accuracy
        self._speed = speed
        self._date = date
        self._batteryInfo = BatteryStatus.BatteryStatus(level, voltage, status, temperature, connected)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def id_trajectory(self):
        return self._id_trajectory

    @id_trajectory.setter
    def id_trajectory(self, value):
        self._id_trajectory = value

    @property
    def obtained(self):
        return self._obtained

    @obtained.setter
    def obtained(self, value):
        self._obtained = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @latitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, value):
        self._altitude = value

    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value):
        self._accuracy = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def batteryInfo(self):
        return self._batteryInfo

    @batteryInfo.setter
    def batteryInfo(self, value):
        self._batteryInfo = value

    def __str__(self):
        return '%d, %d, %i, %f, %f, %f, %s, %s' % \
               (self._id, self._id_trajectory, self._obtained, self._latitude, self._longitude, self._accuracy,
                self._date, self._batteryInfo)
