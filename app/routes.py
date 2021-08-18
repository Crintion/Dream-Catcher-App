from app import db
from app.models.journal_entry import JournalEntry
from flask import Blueprint, request, make_response, jsonify
import requests
import flask_migrate
import os
 
journal_entry_bp = Blueprint("journal_entry", __name__, url_prefix='/journal_entry')



@journal_entry_bp.route("", methods=["POST", "PUT"])
def post_entry():
    request_body = request.get_json()
    new_entry = JournalEntry( 
        calendar_id=request_body["calendar_id"],
        journal_text=request_body["journal_text"],
        journal_mood = request_body["journal_mood"])
    entry = JournalEntry.query.filter_by(calendar_id = request_body["calendar_id"]).first()
    if not entry:
        db.session.add(new_entry)
        db.session.commit()
        return jsonify(request_body), 201
        # return make_response(f"Journal: {new_entry.calendar_id} was successfully created"), 201
    else:
        entry.calendar_id=request_body["calendar_id"]
        entry.journal_text=request_body["journal_text"]
        entry.journal_mood=request_body["journal_mood"]

        db.session.commit()

    return jsonify(request_body), 201 
    # return make_response(f"Journal: {new_entry.calendar_id} was successfully updated"), 200

@journal_entry_bp.route("", methods=["GET"])
def get_all_entries():
    journal_entry_response_body = []
    print(journal_entry_response_body)
    journal_entries = JournalEntry.query.all()
    print(journal_entries)
    for entry in journal_entries:
        journal_entry_response_body.append(entry.to_json())
        print(journal_entry_response_body)
    return jsonify(journal_entry_response_body), 200

@journal_entry_bp.route("/calendar_ids", methods=["GET"])
def get_all_calendar_ids():
    calendar_id_response_body = []
    journal_entries = JournalEntry.query.all()
    for entry in journal_entries:
        calendar_id_response_body.append(entry.calendar_id)
    return jsonify(calendar_id_response_body), 200


    
@journal_entry_bp.route("/journal_entry_id/<journal_entry_id>", methods=["GET"])
def get_entry_by_id(journal_entry_id):
    entry = JournalEntry.query.get(journal_entry_id)
    if not entry:
        return "", 404
    return make_response({"journal_entry": entry.to_json()}), 200


@journal_entry_bp.route("/calendar_id/<calendar_id>", methods=["GET"])
def get_entry_by_calendar_id(calendar_id):
    entry = JournalEntry.query.get(calendar_id)
    if not entry:
        return "", 404
    return make_response({"journal_entry": entry.to_json()}), 200
    


            









