from flask import request, make_response, jsonify,json
from sqlalchemy import func
from posts.models import Posts,postSchema,GeoConverter
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from utils.timestampAdd import timeStamp
db = SQLAlchemy()



def tweet():
    if 'lat' in request.args and 'lon' in request.args :
        lat = request.args['lat']
        lon = request.args['lon']
        around = f'SRID=4326;POINT({lon} {lat})'
        page = request.args.get('page',1,type=int)
        per_page = 10
        tweets = Posts.query.filter(func.ST_Contains(Posts.Location_rect,around)).paginate(page=page,per_page=per_page)
        meta={
            'page':tweets.page,
            'pages':tweets.pages,
            'total_count':tweets.total,
            'prev_page':tweets.prev_num,
            'next_page':tweets.next_num,
            'has_prev':tweets.has_prev,
            'has_next':tweets.has_next
        }
        post_schema = postSchema(many=True)
        output = post_schema.dump(tweets.items)
    
        output = timeStamp(output=output)
        response = make_response(
                   jsonify({'data':output,'meta':meta}),
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


def addtweets():
    json_data = request.json
    data = Posts(text=json_data['text'],user_id=json_data['user_id'],user_name=json_data['user_name'],location_name=json_data['location_name'],lang=json_data['lang'],Locatio_rect=json_data['Location_rect'])
    db.session.add(data)
    db.session.commit()
    return make_response('Success')
