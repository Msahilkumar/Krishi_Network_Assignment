from flask import request, make_response, jsonify
from jinja2 import Undefined
import requests
from utils.forcast import forcast
from utils.geocode import geocode
from flask_sqlalchemy import SQLAlchemy
from weather.models import Locaitons

db = SQLAlchemy()

def index():
    if 'address' in request.args:
        address=request.args['address']
    else :
        response = make_response(
                jsonify(
                    {"message": 'Please provide an address'}
                ),
                401,
            )
        response.headers["Content-Type"] = "application/json"
        return response

    details,error = geocode(address=address)

    if error!=Undefined:
        response = make_response(
                jsonify(
                    {"message": 'Invalid address..! Please try with another address'}
                ),
                401,
            )
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        lat = details['lat']
        lon = details['lon']
        place_name = details['place_name']

        data = Locaitons(place=place_name,Location=f'SRID=4326;POINT({lon} {lat})')
        db.session.add(data)
        db.session.commit()
        response = make_response(
                jsonify(
                    {"message": 'Successfully added to the database..!'}
                ),
                200,
            )
        response.headers["Content-Type"] = "application/json"
        return response


def weather():
    if 'lat' in request.args and 'lon' in request.args :
        lat = request.args['lat']
        lon = request.args['lon']
        weather,error = forcast(lat=lat,lon=lon)
        if(error!=Undefined):
            response = make_response(
                    jsonify(
                        {"message": 'Could not get weather'}
                    ),
                    401,
                )
            response.headers["Content-Type"] = "application/json"
            return response
        else:
            response = make_response(
                    jsonify(weather),
                    200,
                )
            response.headers["Content-Type"] = "application/json"
            return response
    else :
        response = make_response(
                    jsonify(
                        {"message": 'Please provide latitude and longitude'}
                    ),
                    401,
                )
        response.headers["Content-Type"] = "application/json"
        return response
    