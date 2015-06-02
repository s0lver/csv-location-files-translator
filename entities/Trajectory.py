class Trajectory(object):
    def __init__(self, id, id_user, start_time, end_time):
        self._id = id
        self._idUser = id_user
        self._startTime = start_time
        self._endTime = end_time

    def __init__(self, id_user, gps_fixes):
        self._id = 0
        self.id_user = id_user
        self.start_time = gps_fixes[0].date
        self.end_time = gps_fixes[-1].date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def id_user(self):
        return self._idUser

    @id_user.setter
    def id_user(self, value):
        self._idUser = value

    @property
    def start_time(self):
        return self._startTime

    @start_time.setter
    def start_time(self, value):
        self._startTime = value

    @property
    def end_time(self):
        return self._endTime

    @end_time.setter
    def end_time(self, value):
        self._endTime = value

    def __str__(self):
        return '%d, %d, %s, %s' % (self.id, self.id_user, self.start_time, self.end_time)

