from CsvReader import read_gps_fixes_file
from entities.Trajectory import Trajectory
from db import dal

gps_fixes = read_gps_fixes_file('sample-file-smartphone.csv')

trajectory = Trajectory(1, gps_fixes)
dal.add_trajectory(trajectory)
print(trajectory)

for fix in gps_fixes:
    fix.id_trajectory = trajectory.id

dal.add_gps_fixes(gps_fixes)

read_fixes = dal.get_gps_fixes_by_trajectory(trajectory.id)
for fix in read_fixes:
    print(fix)

