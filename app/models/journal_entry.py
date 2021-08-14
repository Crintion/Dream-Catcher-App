from flask import current_app
from app import db

class JournalEntry(db.Model):
    journal_entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    calendar_id = db.Column(db.Integer, nullable = False)
    journal_text = db.Column(db.String, nullable = False)
    journal_mood = db.Column(db.String, nullable = False)

    def to_json(self):
        
        return {
            "calendar_id": self.calendar_id,
            "journal_text" : self.journal_text,
            "journal_mood" : self.journal_mood
        }
