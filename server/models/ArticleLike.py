#-*-coding:utf-8-*-

from server import db
from datetime import datetime

class ArticleLike(db.Model):
    __tablename__ = 'article_like'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    article_id=db.Column(db.Integer,nullable=False)
    user_id=db.Column(db.Integer,nullable=False)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Integer, nullable=False,default=1)
