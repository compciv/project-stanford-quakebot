import requests
from urllib.parse import urlencode
import csv


BASE_URL_ENDPOINT = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
US_LATITUDE_MIN = 24.5
US_LATITUDE_MAX = 50
US_LONGITUDE_MIN = -126.5
US_LONGITUDE_MAX = -65
DEFAULT_LIMIT = 5
DEFAULT_STARTTIME =  '2005-01-01' # by default, USGS API only looks back 30 days
DEFAULT_MIN_MAG=5
ATTRS_TO_KEEP = ['id', 'mag', 'time', 'latitude', 'longitude', 'place']

def make_url_for_recent_big_quakes_in_contiguous_usa(num_results=5):
    """
    A helper function that simply produces the properly formatted
        URL for the USGS API, for the specific definition of "big"
        quakes (M5.0+) a

    Args: a number representing the max number of results
        wanted from the API
    
    Returns:
        str: just a URL
    """


    myparams = {'format': 'csv', 
                'orderby': 'time',
                'limit': num_results,
                'starttime': DEFAULT_STARTTIME,                
                'minmagnitude': DEFAULT_MIN_MAG,
                'minlatitude': US_LATITUDE_MIN,
                'maxlatitude': US_LATITUDE_MAX,
                'minlongitude': US_LONGITUDE_MIN,
                'maxlongitude': US_LONGITUDE_MAX,}

    return BASE_URL_ENDPOINT + urlencode(myparams)


def fetch_recent_big_quakes_in_contiguous_usa(num_results=5):
    """
    Calls the API via `make_url_for_recent_big_quakes_in_contiguous_usa()`
    and returns a list of dicts

    Returns:
        Parses the response from the API and returns a list of dict objects like this:
        [
            {
                'id': 'us2000cpcn'
                'time': '2018-01-25T17:24:33.850Z',
                'latitude': '40.4296'
                'longitude': '-126.3397'
                'mag': '5',
                'place': '180km W of Ferndale, California',
            }            
        ]
    """
    the_url = make_url_for_recent_big_quakes_in_contiguous_usa(num_results)
    resp = requests.get(the_url)
    txt = resp.text
    quakes = list(csv.DictReader(txt.splitlines()))
    data = []
    for q in quakes:
        d = {}
        for attr in ATTRS_TO_KEEP:
            d[attr] = q[attr]
        data.append(d)
    return data