from flask import current_app
from app import db

class DreamEntry(db.Model):
    dream_entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dream_date = db.Column(db.DateTime, nullable=True)
    dream_title = db.Column(db.String)
    dream_text = db.Column(db.String)

    def to_json(self):
        
        return {
            "dream_id" : self.dream_entry_id,
            "dream_title" : self.dream_title,
            "dream_text" : self.dream_text
        }
