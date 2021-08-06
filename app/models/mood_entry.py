from flask import current_app
from app import db

class MoodEntry(db.Model):
    mood_entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mood_entry = db.Column(db.String)
    mood_entry_date = db.Column(db.DateTime, nullable=True)


    def to_json(self):
        
        return {
            "mood_entry_id" : self.mood_entry_id,
            "mood_entry" : self.mood_entry,
            "mood_entry_date" : self.mood_entry_date
        }