from app import db
from app.models.journal_entry import JournalEntry
from app.models.journal_tag import JournalTag
from app.models.mood_entry import MoodEntry
from app.models.mood_tag import MoodTag
from flask import Blueprint, request, make_response, jsonify
from datetime import datetime
import requests
import flask_migrate
import os
 
journal_entry_bp = Blueprint("journal_entry", __name__, url_prefix='/journal_entry')
journal_tag_bp = Blueprint("journal_tag", __name__, url_prefix='/journal_tag')
# mood_entry_bp = Blueprint("mood_entry", __name__, url_prefix='/mood_entry')
# mood_tag_bp = Blueprint("mood_tag", __name__, url_prefix='/mood_tag')

@journal_entry_bp.route("", methods=["POST"], strict_slashes = False)
def post_entry():
    request_body = request.get_json()
    new_entry = JournalEntry(
        journal_date=request_body["journal date"], 
        journal_title=request_body["journal title"],
        journal_text=request_body["journal text"])

    db.session.add(new_entry)
    db.session.commit()

    return make_response(f"Journal: {new_entry.journal_title} was successfully created"), 201

@journal_entry_bp.route("", methods=["GET"], strict_slashes = False)
def get_all_entries():
    journal_entry_response_body = []
    journal_entries = JournalEntry.query.all()
    for entry in journal_entries:
        journal_entry_response_body.append(entry.to_json())
    return jsonify(journal_entry_response_body), 200
    
@journal_entry_bp.route("/<journal_entry_id>", methods=["GET"], strict_slashes = False)
def get_single_entry(journal_entry_id):
    entry = JournalEntry.query.get(journal_entry_id)
    if not entry:
        return "", 404
    return make_response({"Journal entry": entry.to_json()}), 200

@journal_tag_bp.route("", methods=["POST"], strict_slashes = False)
def post_tags():
    request_body = request.get_json()
    new_tag = JournalTag(journal_tag=request_body["journal tag"],
                        journal_tag_date=request_body["journal tag date"])

    db.session.add(new_tag)
    db.session.commit()

    return make_response(f"Tag: {new_tag.journal_tag} was successfully created", 201)

@journal_tag_bp.route("", methods=["GET"], strict_slashes = False)
def get_all_tags():
    tag_response_body = []
    tag_entries = JournalTag.query.all()
    for entry in tag_entries:
        tag_response_body.append(entry.to_json())
    return jsonify(tag_response_body), 200

@journal_tag_bp.route("/<journal_tag_id>", methods=["GET"], strict_slashes = False)
def get_single_tag(journal_tag_id):
    tag = JournalTag.query.get(journal_tag_id)
    if not tag:
        return "", 404
    return make_response({"Journal Tag": tag.to_json()}), 200
