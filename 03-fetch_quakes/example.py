import requests
from urllib.parse import urlencode
import csv

BASE_URL_ENDPOINT = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
MAX_LIMIT = 10
DEFAULT_MIN_MAG = 5
DEFAULT_STARTTIME =  '2005-01-01' # by default, USGS API only looks back 30 days

MIDWEST_LATITUDE_MIN = 33.8
MIDWEST_LATITUDE_MAX = 45.3
MIDWEST_LONGITUDE_MIN = -112.4
MIDWEST_LONGITUDE_MAX = -85.7

print("Getting the most recent 10 earthquakes with magnitude of at least M5.0+ in the Midwest")
print("...")
myparams = {'format': 'csv', 
            'orderby': 'time',
            'limit': MAX_LIMIT,
            'minmagnitude': DEFAULT_MIN_MAG,
            'starttime': DEFAULT_STARTTIME, 
            'minlatitude': MIDWEST_LATITUDE_MIN,
            'maxlatitude': MIDWEST_LATITUDE_MAX,
            'minlongitude': MIDWEST_LONGITUDE_MIN,
            'maxlongitude': MIDWEST_LONGITUDE_MAX,
            }

the_url = BASE_URL_ENDPOINT + urlencode(myparams)
print("Fetching from:", the_url)
resp = requests.get(the_url)

txt = resp.text
quakes = list(csv.DictReader(txt.splitlines()))

for q in quakes:
    msg = 'At {t}, USGS detected a {m}M quake near {p}'.format(m=q['mag'], p=q['place'], t=q['time'])
    print(msg)





