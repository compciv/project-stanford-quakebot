import gmaps_api
import mapmath # expects this module to contain functions for calculating distance
import usgs_api

MSG_TEMPLATE = \
"""
On {datetime}, the USGS detected a M{mag}
earthquake {description} -- which is about
{dist_from_stanford} km from Stanford University.

USGS official page: {usgs_url}

Google Map: {gmaps_url}
"""    

def stanford_quake_bot(num_entries):
    """
    Fetches the n (5 by default) most recent M5.0+ earthquakes in the 
    contiguous U.S. from the USGS API, 
    and creates messages ready for tweeting that describe the detected quake and
    its distance from Stanford, with contextual URLs (such as Google Maps)

    Example usage:

        for msg in stanford_quake_bot(3):
            print("---")
            print(msg)

    Args:
        A number of quakes to ask the API for. By default, it should be 5    
    Returns:
        str: a text message ready to be tweeted
    """
   messages = {}
   quakes = usgs_api.fetch_recent_big_quakes_in_contiguous_usa(num_entries)
   
   for q in quakes:
       msg = MSG_TEMPLATE.format({
           'id': q['id'],
           'magnitude': q['mag'],
           'datetime': q['time'],
           'description': q['place'],
           'usgs_url': 'https://earthquake.usgs.gov/earthquakes/eventpage/{id}#executive'.format(id=q['id']),
           'gmaps_url'
       })
       make_url_for_directions_to_stanford()


