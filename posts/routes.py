from flask import Blueprint


from posts.controller import tweet,addtweets

post_bp = Blueprint('post_bp', __name__)

post_bp.route('/', methods=['GET']) (tweet)
post_bp.route('/add',methods=['POST'])(addtweets)