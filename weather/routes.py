from flask import Blueprint


from weather.controller import index,weather

weather_bp = Blueprint('weather_bp', __name__)

weather_bp.route('/weather',methods=['GET']) (weather)
weather_bp.route('/add',methods=['POST']) (index)
