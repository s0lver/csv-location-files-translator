import simplekml

def create_pinned(path, fixes):
    kml = simplekml.Kml()
    i = 1
    for fix in fixes:
        kml.newpoint(name='point%d' % i, coords=[(fix.longitude, fix.latitude, fix.altitude)])
        i += 1

    kml.save(path)
    print('KML file %s created' % path)

def create_pinned_timed(path, fixes):
    kml = simplekml.Kml()
    i = 1
    for fix in fixes:
        p = kml.newpoint(name='point%d' % i, coords=[(fix.longitude, fix.latitude, fix.altitude)])
        p.timestamp.when = fix.date.strftime('%Y-%m-%dT%H:%M:%SZ')
        i += 1

    kml.save(path)
    print('KML file %s created' % path)

def create_lined(path, fixes):
    kml = simplekml.Kml()
    coordinates = []

    for fix in fixes:
        coordinates.append((fix.longitude, fix.latitude, fix.altitude))

    ls = kml.newlinestring(name='trajectory', description='-', coords=coordinates)
    ls.altitudemode = simplekml.AltitudeMode.relativetoground
    ls.style.linestyle.width = 5
    ls.style.linestyle.color = simplekml.Color.red

    kml.save(path)
    print('KML file %s created' % path)
