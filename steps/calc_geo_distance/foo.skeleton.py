def calc_geo_distance(longitude_1, latitude_1, longitude_2, latitude_2):
  """
  Uses the Haversine formula to calculate distance between two geospatial points

  Args:
    longitude_1, latitude_1, longitude_2, latitude_2: float
      These 4 float values represent 2 coordinate pairs, i.e. points on Earth, as expressed in latitude and longitude decimal degrees

  Returns:
    float: the distance between points in kilometers
  """
