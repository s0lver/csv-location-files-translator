import csv
from entities import GpsFix, StayPoint
from datetime import datetime

def create_gps_fix(row):
    id = 0
    id_trajectory  = 0
    obtained = True if row[0] == 'Si' else False
    latitude = float(row[1])
    longitude = float(row[2])
    altitude = float(row[3])
    accuracy = float(row[4])
    speed = float(row[5])
    date = datetime.strptime(row[6], '%a %b %d %H:%M:%S CDT %Y')
    level = float(row[7])
    voltage = float(row[8])
    status = row[9]
    temperature = float(row[10])
    connected = row[11]
    return GpsFix.GpsFix(id, id_trajectory, obtained, latitude, longitude, altitude, accuracy, speed, date,
                         level, voltage, status, temperature, connected)

def create_staypoint(row):
    latitude = float(row[0])
    longitude = float(row[1])
    arrival_time = datetime.strptime(row[2], '%d/%m/%Y %H:%M:%S')
    departure_time = datetime.strptime(row[3], '%d/%m/%Y %H:%M:%S')
    amount_fixes_involved = int(row[4])

    return StayPoint.StayPoint(latitude, longitude, arrival_time, departure_time, amount_fixes_involved)


def read_gps_fixes_file(path):
    file = open(path)
    csv_file = csv.reader(file)

    gps_fixes = []

    for row in csv_file:
        fix = create_gps_fix(row)
        gps_fixes.append(fix)

    return gps_fixes


def read_staypoints_file(path):
    file = open(path)
    csv_file = csv.reader(file)

    staypoints = []
    for row in csv_file:
        staypoint = create_staypoint(row)
        staypoints.append(staypoint)

    return staypoints

"""
Description of the smartphone csv file structure
Pos     :meaning
0:  whether reading was obtained "Si" : "No"
1:  latitude
2:  longitude
3:  altitude
4:  accuracy
5:  speed
6:  timestamp
7:  battery level
8:  voltage
9:  status
10: temperature
11: plugged
"""

"""
Description of the staypoints file
Pos     :meaning
0:      latitude
1:      longitude
2:      arrival_time
3:      departure_time
4:      amount_fixes_involved
"""