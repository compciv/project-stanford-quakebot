from math import sin, cos, sqrt, atan2, radians

EARTH_RADIUS_IN_KM = 6373.0

latitude_1 = 52.2296756
longitude_1 = 21.0122287
latitude_2 = 52.406374
longitude_2 = 16.9251681

lat1 = radians(latitude_1)
lon1 = radians(longitude_1)
lat2 = radians(latitude_2)
lon2 = radians(longitude_2)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = EARTH_RADIUS_IN_KM * c

print("Distance:", distance, "km")

# Modified, refactored version of:
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude/19412565#19412565
