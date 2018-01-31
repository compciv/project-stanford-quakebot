# This script expects the following file to exist:
# requires downloading CSV file from the  following URL
# https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2018-01-25&endtime=2018-01-26&minmagnitude=5&minlatitude=24.5&maxlatitude=50&minlongitude=-126.5&maxlongitude=-65&orderby=time-asc

import csv
DATA_FILENAME = 'quakes_cache.csv'
MSG_TEMPLATE = """
A {mag}M earthquake was detected {desc}. 
Official USGS page: 
{url}
"""

df = open(DATA_FILENAME, 'r')
txt = df.read()
df.close()

lines = txt.splitlines()
quakes = list(csv.DictReader(lines))

for q in quakes:
    usgsurl = 'https://earthquake.usgs.gov/earthquakes/eventpage/{id}#executive'.format(id=q['id'])
    msg = MSG_TEMPLATE.format(mag=q['mag'], desc=q['place'], url=usgsurl)
    print(msg)








