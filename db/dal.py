from db import QueryRunner as qr
from entities.GpsFix import GpsFix

def save_trajectory(trajectory):
    """
    Inserts a trajectory and updates it with the inserted id
    :param trajectory: trajectory object
    :return:
    """
    query = "INSERT INTO trajectories (idUser, startTime, endTime) VALUES (%(id_user)s, %(start_time)s, %(end_time)s)"

    trajectory_data = {
        'id_user': trajectory.id_user,
        'start_time': trajectory.start_time,
        'end_time': trajectory.end_time
    }

    inserted_id = qr.run_write_query(query, trajectory_data)
    trajectory.id = inserted_id

def save_gps_fix(fix):
    """
    Inserts a GpsFix and updates it with the inserted id
    :param fix: fix object
    :return:
    """
    raw_query = ('INSERT INTO smartphonefixes',
                 '(idTrajectory, obtained, latitude, longitude, height, accuracy, speed,',
                 'timestamp, batteryLevel, voltage, status, temperature, plugged)',
                 'VALUES (%(id_trajectory)s, %(obtained)s, %(latitude)s, %(longitude)s, %(height)s,',
                 '%(accuracy)s, %(speed)s,',
                 '%(date)s, %(battery_level)s, %(voltage)s, %(status)s, %(temperature)s, %(plugged)s )')

    query = " ".join(raw_query)

    fix_data = {
        'id_trajectory': fix.id_trajectory,
        'obtained': fix.obtained,
        'latitude': fix.latitude,
        'longitude': fix.longitude,
        'height': fix.altitude,
        'accuracy': fix.accuracy,
        'speed': fix.speed,
        'date': fix.date,
        'battery_level': fix.batteryInfo.level,
        'voltage': fix.batteryInfo.voltage,
        'status': fix.batteryInfo.status,
        'temperature': fix.batteryInfo.temperature,
        'plugged': fix.batteryInfo.plugged
    }

    inserted_id = qr.run_write_query(query, fix_data)
    fix.id = inserted_id

def save_gps_fixes(fixes):
    """
    Inserts the list of fixes
    :param fixes: List of fixes to insert
    :return:
    """
    raw_query = ('INSERT INTO smartphonefixes',
                 '(idTrajectory, obtained, latitude, longitude, height, accuracy, speed,',
                 'timestamp, batteryLevel, voltage, status, temperature, plugged)',
                 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )')

    query = " ".join(raw_query)
    flat_fixes = []

    for fix in fixes:
        flat_fixes.append((fix.id_trajectory, fix.obtained, fix.latitude, fix.longitude, fix.altitude, fix.accuracy,
                           fix.speed, fix.date, fix.batteryInfo.level, fix.batteryInfo.voltage,
                           fix.batteryInfo.status, fix.batteryInfo.temperature, fix.batteryInfo.plugged))

    qr.run_write_many_query(query, flat_fixes)

def get_gps_fixes_by_trajectory(id_trajectory):
    """
    Obtains the list of fixes of the given trajectory
    :param id_trajectory: The id of the trajectory to look
    :return:
    """
    query = "SELECT * FROM smartphonefixes WHERE idTrajectory = %(id_trajectory)s"
    select_data = {'id_trajectory': id_trajectory}

    fixes = qr.run_read_query(query, select_data)

    gps_fixes = []
    for fix in fixes:
        gps_fixes.append(GpsFix(fix[0], fix[1], fix[2], fix[3], fix[4], fix[5], fix[6], fix[7],
                                fix[8], fix[9], fix[10], fix[11], fix[12], fix[13]))

    return gps_fixes
