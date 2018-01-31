import mapmath # expects this module to contain functions for calculating distance
import usgs_api
import gmaps_api

MSG_TEMPLATE = \
"""
On {datetime}, the USGS detected a M{mag}
earthquake {description} -- which is about
{dist_from_stanford} km from Stanford University.

USGS official page: {usgs_url}

Google Map: {gmaps_url}
"""    


def message_maker(num_entries):
    """
    Fetches the num_entries (5 by default) most recent M5.0+ earthquakes in the 
    contiguous U.S. from the USGS API, 
    and creates messages ready for tweeting that describe the detected quake and
    its distance from Stanford, with contextual URLs (such as Google Maps)

    Args:
        num_entries: A number of quakes to ask the API for. By default, it should be 5    
    Returns:
        list: a list of strings, ready to be tweeted
    Example usage:

        messages = message_maker(3)
        for msg in messages:
            print("\n---")
            print(msg)
    """



