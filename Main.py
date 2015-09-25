import os
from CsvReader import read_staypoints_file
from CsvReader import read_gps_fixes_file
from input.dummy_data import create_test_fixes
from algorithms.montoliou import montoliou_algorithm
from algorithms.zhen import zhen_algorithm
from maps import kml_creator

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

# suggested_root_directory = "~/Dropbox/cinvestav/doctorado/methodology/location-data/gps-data/victoria/"
suggested_root_directory = "~/Desktop/"
root_directory = ""

# Ask for directory
use_suggested = input("Want to use suggested root directory? 1)YES, 2) NO : ")
if (use_suggested == '1'):
    root_directory = input("Root address (starting from " + suggested_root_directory + "): ")
    root_directory = suggested_root_directory + root_directory
else:
    root_directory = input("Enter full directory path: ")

root_directory =  os.path.expanduser(root_directory)
print("Specified root directory is " + root_directory)
directory_exists = os.path.exists(root_directory)
directory_is_actually_a_directory = os.path.isdir(root_directory)

# Traverse over directory
if (directory_exists and directory_is_actually_a_directory):
    for file in os.listdir(root_directory):
        if file.endswith(".csv"):
            filename = os.path.splitext(file)[0];
            print("Processing file " + filename)
            is_staypoints_file = filename.__contains__("staypoint")
            # Do according to filetype
            if (is_staypoints_file):
                print("Processing sp file: " + filename)
                staypoints = read_staypoints_file(root_directory + file)
                output_file = root_directory + filename + "_pinned.kml"
                kml_creator.create_pinned_for_staypoints(output_file, staypoints)
            else:
                gps_fixes = read_gps_fixes_file(root_directory + file)
                output_file = root_directory + filename + "_pinned.kml"
                kml_creator.create_pinned_for_fixes(output_file,gps_fixes)

                output_file = root_directory + filename + "_pinned_timed.kml"
                kml_creator.create_pinned_timed_for_fixes(output_file,gps_fixes)

                output_file = root_directory + filename + "_lined.kml"
                kml_creator.create_lined_for_fixes(output_file,gps_fixes)
else:
    print("bad directory input")
