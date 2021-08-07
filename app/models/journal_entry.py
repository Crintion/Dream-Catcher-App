from flask import current_app
from app import db

class JournalEntry(db.Model):
    journal_entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    journal_month = db.Column(db.Integer, nullable = False)
    journal_day = db.Column(db.Integer, nullable = False)
    journal_title = db.Column(db.String, nullable = False)
    journal_text = db.Column(db.String, nullable = False)
    journal_mood = db.Column(db.String, nullable = False)

    def to_json(self):
        
        return {
            "journal_month" : self.journal_month,
            "journal_day" : self.journal_day,
            "journal_title" : self.journal_title,
            "journal_text" : self.journal_text,
            "journal_mood" : self.journal_mood
        }
