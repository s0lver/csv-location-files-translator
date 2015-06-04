from input.dummy_data import create_test_fixes
from algorithms.montoliou import montoliou_algorithm
from algorithms.zhen import zhen_algorithm
from maps import kml_creator
import maps.kml_creator
# from CsvReader import read_gps_fixes_file
# from entities.Trajectory import Trajectory
# from db import dal

# gps_fixes = read_gps_fixes_file('fixes-2.csv')
#
# # Create and save trajectory
# trajectory = Trajectory(1, gps_fixes)
# dal.save_trajectory(trajectory)
#
# # Update the id_trajectory in fixes
# for fix in gps_fixes:
#     fix.id_trajectory = trajectory.id
#
# # Save fixes
# dal.save_gps_fixes(gps_fixes)
#
# # Show fixes obtained from database
# read_fixes = dal.get_gps_fixes_by_trajectory(trajectory.id)
# for fix in read_fixes:
#     print(fix)

# print('Montoliou')
fixes = create_test_fixes()
# sp_montoliou = montoliou_algorithm(fixes, 60, 3600, 150, True)
# print('Stay points')
# for sp in sp_montoliou:
#     print(sp)
#
# print('')
# print('Zhen')
# sp_zhen = zhen_algorithm(fixes, 60, 150, True)
# print('Stay points')
# for sp in sp_zhen:
#     print(sp)

# kml_creator.create_pinned('pinned.kml', fixes)
# kml_creator.create_lined('lined.kml', fixes)
kml_creator.create_pinned_timed('pinned-timed.kml', fixes)
