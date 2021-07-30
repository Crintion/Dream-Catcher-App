from flask import current_app
from app import db

class DreamTag(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dream_tag = db.Column(db.String)


    def to_json(self):
            
            return {
                "tag_id" : self.tag_id,
                "dream_tag" : self.dream_tag
            }