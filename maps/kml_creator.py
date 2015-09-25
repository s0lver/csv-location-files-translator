import simplekml


def create_pinned_for_fixes(path, fixes):
    kml = simplekml.Kml()
    i = 1
    for fix in fixes:
        if (fix.obtained == True):
            kml.newpoint(name='point%d' % i, coords=[(fix.longitude, fix.latitude)])
            i += 1

    kml.save(path)
    print('KML file %s created' % path)


def create_pinned_timed_for_fixes(path, fixes):
    kml = simplekml.Kml()
    i = 1
    for fix in fixes:
        if (fix.obtained == True):
            p = kml.newpoint(name='point%d' % i, coords=[(fix.longitude, fix.latitude)])
            p.timestamp.when = fix.date.strftime('%Y-%m-%dT%H:%M:%SZ')
            i += 1

    kml.save(path)
    print('KML file %s created' % path)


def create_lined_for_fixes(path, fixes):
    kml = simplekml.Kml()
    coordinates = []
    for fix in fixes:
        if (fix.obtained == True):
            # coordinates.append((fix.longitude, fix.latitude,altitude))
            coordinates.append((fix.longitude, fix.latitude))

    ls = kml.newlinestring(name='trajectory', description='-', coords=coordinates)
    ls.altitudemode = simplekml.AltitudeMode.relativetoground
    ls.style.linestyle.width = 5
    ls.style.linestyle.color = simplekml.Color.red

    kml.save(path)
    print('KML file %s created' % path)


def create_pinned_for_staypoints(path, staypoints):
    altitude = 0
    kml = simplekml.Kml()
    i = 1

    point_style = simplekml.Style()
    point_style.labelstyle.color = simplekml.Color.green  # Make the text red
    point_style.labelstyle.scale = 1  # Make the text twice as big
    #point_style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    point_style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/info-i.png'
    point_style.iconstyle.scale = 2

    for staypoint in staypoints:
        point = kml.newpoint(name='Staypoint%d' % i,  coords=[(staypoint.long, staypoint.lat)])
        point.style = point_style

        i += 1

    kml.save(path)
    print('KML file %s created' % path)
