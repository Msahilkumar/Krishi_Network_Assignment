from jinja2 import Undefined
import config
import requests

def forcast(lat,lon) :
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid='+config.appid+'&units=imperial'

    response = requests.get(url).json()
    if(response.get('cod')!=200) :
        return (Undefined,'Unable to find locaiton, Please try with another search')
    else :
        weather = {
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }
        return (weather,Undefined)
