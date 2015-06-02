class BatteryStatus(object):
    def __init__(self, level, voltage, status, temperature, plugged):
        self._level = level
        self._voltage = voltage
        self._status = status
        self._temperature = temperature
        self._plugged = plugged

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        self._voltage = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def plugged(self):
        return self._plugged

    @plugged.setter
    def plugged(self, value):
        self._plugged = value

    def __str__(self):
        return '%.2f, %.1f, %s, %d, %s' % \
               (self.level, self.voltage, self.status, self.temperature, self.plugged)

