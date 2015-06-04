from entities import GpsFix
from datetime import datetime


def create_test_fixes():
    sample_fixes = []
    fix = GpsFix.GpsFix(0, 0, True, 24.840481, -98.166489, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 13:47:20 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.84123, -98.164726, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 13:50:20 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.841026, -98.163269, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 13:52:25 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.842857, -98.156059, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 14:02:10 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.844316, -98.155846, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 14:04:21 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.845079, -98.155792, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 14:05:33 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.845606, -98.155815, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 14:06:38 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.846004, -98.155792, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 14:14:44 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.849789, -98.155647, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 14:15:39 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)
    fix = GpsFix.GpsFix(0, 0, True, 24.850178, -98.155594, 0.0, 0.0, 0.0,
                        datetime.strptime("Tue May 15 14:16:32 CDT 2012", '%a %b %d %H:%M:%S CDT %Y'), 0, 0, 'ok', 0,
                        'unplugged')
    sample_fixes.append(fix)

    return sample_fixes
