from urllib.parse import urlencode

STANFORD_LAT = 37.424107
STANFORD_LNG = -122.166077

BASE_API_ENDPOINT = 'https://www.google.com/maps/dir/'


def make_url_for_directions(origin, destination):
    """
    Given two coordinate pairs, returns a proper Google Maps directions URL

    Example usage:
        make_url_for_directions({'lat': 37.4, 'lng': -122.1}, {'lat': 42, 'lng': -110})

    Example output:

    Arguments:
        Two dicts, origin and destination, each having 'lat' and 'lng' as attributes


    Returns:
        str: just the URL
    """
    o_lat = origin['lat']
    o_lng = origin['lng']
    d_lat = destination['lat']
    d_lng = destination['lng']
    gmap_params = {'api': 1, 
                   'origin': '{},{}'.format(o_lat, o_lng), 
                   'destination': '{},{}'.format(d_lat, d_lng)}

    paramstr = urlencode(gmap_params)
    return BASE_API_ENDPOINT + '?' + paramstr


def make_url_for_directions_to_stanford(destination):
    """
    literally just one line almost

    Arguments: 
        destination: this is a dict: {'lat': 99, 'lng': 42}

    Returns:
        str: just a URL
    """

    s_latlng = {'lat': STANFORD_LAT, 'lng': STANFORD_LNG }
    return make_url_for_directions(s_latlng, destination)
