from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

EARTH_RADIUS = 6373.0
KM_PER_MILE = 0.621371

STANFORD_LAT = 37.424107
STANFORD_LNG = -122.166077  

def calc_distance_from_any_two_points(origin_lat, origin_lng, dest_lat, dest_lng):
    """
    Returns the distance (in km) from one  geospatial point (i.e. latitude and longitude)
       to another.

    Example usage:
        calc_distance_from_stanford(origin_lat=-38.2, origin_lng=-112.5, dest_lat=-45, dest_lng=-110)
    """

    lat_1 = radians(origin_lat)
    lon_1 = radians(origin_lng)
    lat_2 = radians(dest_lat)
    lon_2 = radians(dest_lng)

    dlon = lon_2 - lon_1
    dlat = lat_2 - lat_1

    a = sin(dlat / 2)**2 + cos(lat_1) * cos(lat_2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance_km = EARTH_RADIUS * c
    return distance_km


def calc_distance_from_stanford(lat, lng):
    """
    Returns the distance (in km) from a given geospatial point (i.e. latitude and longitude)
       to Stanford's campus. Basically calls calc_distance_from_any_two_points(), except with 
        the coordinates for Stanford hardcoded as the origin

    Example usage:
        calc_distance_from_stanford(lat=-38.2, lng=112.5)

    Hint: this functon should be only one line
    """ 
    return calc_distance_from_any_two_points(STANFORD_LAT, STANFORD_LNG, lat, lng)