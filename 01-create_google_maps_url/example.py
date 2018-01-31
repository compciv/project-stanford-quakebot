from urllib.parse import urlencode

STANFORD_LAT = 37.424107
STANFORD_LNG = -122.166077
NYC_LAT = 40.785091
NYC_LNG = -73.968285

BASE_API_ENDPOINT = 'https://www.google.com/maps/dir/'

gmap_params = {'api': 1, 
               'origin': '{},{}'.format(STANFORD_LAT, STANFORD_LNG), 
               'destination': '{},{}'.format(NYC_LAT, NYC_LNG)
             }

paramstr = urlencode(gmap_params)

gmaps_url = BASE_API_ENDPOINT + '?' + paramstr

print(gmaps_url)
