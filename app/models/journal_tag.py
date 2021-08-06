from flask import current_app
from app import db

class JournalTag(db.Model):
    journal_tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    journal_tag = db.Column(db.String)
    journal_tag_date = db.Column(db.DateTime, nullable=True)


    def to_json(self):
            
            return {
                "journal_tag_id" : self.journal_tag_id,
                "journal_tag" : self.journal_tag,
                "journal_tag_date" : self.journal_tag_date
            }