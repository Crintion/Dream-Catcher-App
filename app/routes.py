from app import db
from app.models.journal_entry import JournalEntry
from flask import Blueprint, request, make_response, jsonify
from datetime import datetime
import requests
import flask_migrate
import os
 
journal_entry_bp = Blueprint("journal_entry", __name__, url_prefix='/journal_entry')



@journal_entry_bp.route("", methods=["POST", "PUT"])
def post_entry():
    request_body = request.get_json()
    new_entry = JournalEntry(
        journal_month=request_body["journal month"],
        journal_day=request_body["journal day"], 
        journal_title=request_body["journal title"],
        journal_text=request_body["journal text"],
        journal_mood = request_body["journal mood"])
    entry = JournalEntry.query.filter_by(journal_month = request_body["journal month"], journal_day = request_body["journal day"]).first()
    if not entry:
        db.session.add(new_entry)
        db.session.commit()
        return make_response(f"Journal: {new_entry.journal_title} was successfully created"), 201
    else:
        entry.journal_title=request_body["journal title"]
        entry.journal_text=request_body["journal text"]
        entry.journal_mood=request_body["journal mood"]

        db.session.commit()
        
    return make_response(f"Journal: {new_entry.journal_title} was successfully updated"), 200

@journal_entry_bp.route("", methods=["GET"])
def get_all_entries():
    journal_entry_response_body = []
    journal_entries = JournalEntry.query.all()
    for entry in journal_entries:
        journal_entry_response_body.append(entry.to_json())
    return jsonify(journal_entry_response_body), 200
    
@journal_entry_bp.route("/<journal_entry_id>", methods=["GET"])
def get_entry_by_id(journal_entry_id):
    entry = JournalEntry.query.get(journal_entry_id)
    if not entry:
        return "", 404
    return make_response({"Journal entry": entry.to_json()}), 200

@journal_entry_bp.route("/month/<journal_month>/day/<journal_day>", methods=["GET"])
def get_entry_by_date(journal_month, journal_day):
    entry = JournalEntry.query.filter_by(journal_month = journal_month, journal_day = journal_day).first()
    if not entry:
        return "", 404
    return make_response({"Journal entry": entry.to_json()}), 200

@journal_entry_bp.route("/month/<journal_month>/day/<journal_day>", methods=["DELETE"])
def delete_entry(journal_month, journal_day):
    entry = JournalEntry.query.filter_by(journal_month = journal_month, journal_day = journal_day).first()
    if not entry:
        return "", 404
    else:
        db.session.delete(entry)
        db.session.commit()
    return make_response("Journal entry deleted"), 200
            









