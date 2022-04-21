from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column , String,Integer,Text, func,DateTime
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelConverter
from marshmallow import fields
from geoalchemy2 import Geometry

db = SQLAlchemy()
ma  = Marshmallow()

class Posts(db.Model):
    __tablename__='posts'
    id=Column(Integer,primary_key=True)
    text = Column(Text)
    user_id= Column(String(200))
    user_name=Column(String(200))
    location_name=Column(String(200))
    lang = Column(String(20))
    Location_rect = Column(Geometry(geometry_type='POLYGON', srid=4326))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    def __init__(self,text,user_id,user_name,location_name,lang,Locatio_rect) :
        self.text=text
        self.user_id =user_id
        self.user_name=user_name
        self.location_name=location_name
        self.lang=lang
        self.Location_rect=Locatio_rect


class GeoConverter(ModelConverter):
    SQLA_TYPE_MAPPING = ModelConverter.SQLA_TYPE_MAPPING.copy()
    SQLA_TYPE_MAPPING.update({
        Geometry: fields.Str
    })

class postSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Posts
        model_converter=GeoConverter