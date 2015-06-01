import entities
from entities import BatteryStatus


class GpsFix(object):
    def __init__(self, obtained, latitude, longitude, accuracy, date, level, voltage, status, temperature, connected):
        self._obtained = obtained
        self._latitude = latitude
        self._longitude = longitude
        self._accuracy = accuracy
        self._date = date
        self._batteryInfo = BatteryStatus.BatteryStatus(level, voltage, status, temperature, connected)

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
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value):
        self._accuracy = value

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
        return '%f, %f, %f, %s, %s' % \
               (self._latitude, self._longitude, self._accuracy, self._date, self._batteryInfo)
