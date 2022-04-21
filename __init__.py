from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from weather.routes import weather_bp
from posts.routes import post_bp
import config
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

app.register_blueprint(weather_bp, url_prefix='/')
app.register_blueprint(post_bp,url_prefix='/posts')


