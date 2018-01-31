from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

EARTH_RADIUS = 6373.0
KM_PER_MILE = 0.621371

STANFORD_LAT = 37.424107
STANFORD_LNG = -122.166077  

NY_CENTRAL_PARK_LAT = 40.785091
NY_CENTRAL_PARK_LNG = -73.968285  

lat_1 = radians(STANFORD_LAT)
lon_1 = radians(STANFORD_LNG)
lat_2 = radians(NY_CENTRAL_PARK_LAT)
lon_2 = radians(NY_CENTRAL_PARK_LNG)

dlon = lon_2 - lon_1
dlat = lat_2 - lat_1

a = sin(dlat / 2)**2 + cos(lat_1) * cos(lat_2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance_km = EARTH_RADIUS * c
distance_mi = distance_km * KM_PER_MILE

answertxt = 'Distance from Stanford to NYC Central Park is: {km} km, or: {mi} mi.'

print(answertxt.format(km=round(distance_km, 1), mi=round(distance_mi, 1)))