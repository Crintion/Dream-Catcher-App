from flask import current_app
from app import db

class JournalEntry(db.Model):
    journal_entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    journal_date = db.Column(db.String, nullable=True)
    journal_title = db.Column(db.String)
    journal_text = db.Column(db.String)
    journal_color = db.Column(db.String)

    def to_json(self):
        
        return {
            "journal_date" : self.journal_date,
            "journal_title" : self.journal_title,
            "journal_text" : self.journal_text,
            "journal_color" : self.journal_color
        }
