from flask import current_app
from app import db

class MoodTag(db.Model):
    mood_tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mood_tag = db.Column(db.String)
    mood_tag_date = db.Column(db.DateTime, nullable=True)


    def to_json(self):
        
        return {
            "mood_tag_id" : self.mood_tag_id,
            "mood_tag" : self.mood_tag,
            "mood_tag_date" : self.mood_tag_date
        }