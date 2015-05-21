import csv
from datetime import datetime

moviles = list()

with open('data/moviles.csv', 'rb') as csvfile:
    moviles_reader = csv.reader(csvfile, delimiter=',', quotechar='"')


    for row in moviles_reader:
        if not row[0] =='MOVIL':
            record = [int(row[1]), row[2], row[5], row[6]]
            moviles.append(record)
        else:
            pass

moviles.sort()


f = open('moviles.gpx', 'w')

f.write('<?xml version="1.0"?>\n')
f.write('<gpx version="1.1" creator="GDAL 1.10.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.topografix.com/GPX/1/1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">\n')
f.write('<metadata>\n')
f.write('<bounds minlat="-34.555209880000000" minlon="-58.492337470000002" maxlat="-34.541080000000001" maxlon="-58.469946380000003"/>\n')
f.write('</metadata>\n')

f.write('<trk>')
f.write('<name/>')
f.write('<type/>')
f.write('<desc/>')
f.write('<trkseg>\n')
for movil in moviles:
    f.write('<trkpt ')
    f.write('lat="')
    f.write(movil[2])
    f.write('" ')

    f.write('lon="')
    f.write(movil[3])
    f.write('"')

    f.write('>')

    f.write('<time>')

    print movil[1]
    print movil[0]
    date_object = datetime.strptime(movil[1], '%d/%m/%Y %H:%M')
    print date_object
    f.write(date_object.strftime('%Y-%m-%dT%H:%M:%SZ'))
    f.write('</time>')

    f.write('</trkpt>')
    f.write('\n')
    
f.write('</trkseg>\n')
f.write('</trk>\n')
f.write('</gpx>\n')