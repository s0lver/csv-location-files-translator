import csv
from entities import GpsFix
from datetime import datetime

def create_gps_fix(row):
    id = 0
    id_trajectory  = 0
    obtained = True if row[0] == 'Si' else False
    latitude = float(row[1])
    longitude = float(row[2])
    height = 0
    speed = 0
    accuracy = float(row[3])
    date = datetime.strptime(row[4],'%a %b %d %H:%M:%S CDT %Y')
    level = float(row[5])
    voltage = float(row[6])
    status = row[7]
    temperature = float(row[8])
    connected = row[9]
    return GpsFix.GpsFix(id, id_trajectory, obtained, latitude, longitude, height, accuracy, speed, date,
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
0       :Whether reading was obtained or not [Si = Yes| No = No]
1       :Latitude
2       :Longitude
3       :Accuracy
4       :Date Format ('Fri May 29 23:36:32 CDT 2015')
5       :Battery level
6       :Voltage
7       :Status (Charging, discharging)
8       :Temperature
9       :Connected (Unplugged, plugged, USB)
"""
