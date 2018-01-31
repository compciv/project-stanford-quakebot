from math import sin, cos, sqrt, atan2, radians
EARTH_RADIUS_IN_KM = 6373.0

def calc_geo_distance(longitude_1, latitude_1, longitude_2, latitude_2):
    """
    Uses the Haversine formula to calculate distance between two geospatial points

    Args:
        longitude_1, latitude_1, longitude_2, latitude_2: float
          These 4 float values represent 2 coordinate pairs, i.e. points on Earth, as expressed in latitude and longitude decimal degrees

    Returns:
        float: the distance between points in kilometers
    """

    lat1 = radians(latitude_1)
    lon1 = radians(longitude_1)
    lat2 = radians(latitude_2)
    lon2 = radians(longitude_2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS_IN_KM * c
