from jinja2 import Undefined
import config
import requests

def geocode(address):
    url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token='+config.access_token+'&limit=1'
    response = requests.get(url.format(address)).json()
    if len(response['features'])==0:
        return ( Undefined,"Unable to find the location ,Please try another search")
    else :
        details ={
            'place_name' : response['features'][0]['place_name'] ,
            'lat' : response['features'][0]['center'][1],
            'lon' : response['features'][0]['center'][0]
        }
        return (details,Undefined)