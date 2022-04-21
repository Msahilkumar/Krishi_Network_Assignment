from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column , String,Integer,Text, func,DateTime
from geoalchemy2 import Geometry

db = SQLAlchemy()

class Locaitons(db.Model):
    __tablename__='locations'
    id = Column(Integer,primary_key=True)
    place = Column(String(200))
    Location = Column(Geometry(geometry_type='POINT', srid=4326))

    def __init__(self,place,Location):
        self.place=place
        self.Location = Location