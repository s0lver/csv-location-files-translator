import csv
from entities import GpsFix
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
    date = datetime.strptime(row[6],'%a %b %d %H:%M:%S CDT %Y')
    level = float(row[7])
    voltage = float(row[8])
    status = row[9]
    temperature = float(row[10])
    connected = row[11]
    return GpsFix.GpsFix(id, id_trajectory, obtained, latitude, longitude, altitude, accuracy, speed, date,
                         level, voltage, status, temperature, connected)

def read_gps_fixes_file(path):
    file = open(path)
    csv_file = csv.reader(file)

    gps_fixes = []

    for row in csv_file:
        fix = create_gps_fix(row)
        gps_fixes.append(fix)

    return gps_fixes

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
Structure of the staypoints (unused here)
return String.format("%f,%f,%s,%s,%d", getLatitude(), getLongitude(),
                simpleDateFormat.format(getArrivalTime()), simpleDateFormat.format(getDepartureTime()),
                getAmountFixesInvolved());
"""