from app import db
from app.models.dream_entry import DreamEntry
from app.models.dream_tag import DreamTag
from flask import Blueprint, request, make_response, jsonify
from datetime import datetime
import requests
import flask_migrate
import os

journal_entry_bp = Blueprint("journal_entry", __name__, url_prefix='/journal_entry')
dream_tag_bp = Blueprint("dream_tag", __name__, url_prefix='/dream_tag')

@journal_entry_bp.route("", methods=["POST"], strict_slashes = False)
def post_entry():
    request_body = request.get_json()
    new_dream = DreamEntry(dream_date=request_body["dream date"], dream_title=request_body["dream title"],
                            dream_text=request_body["dream text"])

    db.session.add(new_dream)
    db.session.commit()

    return make_response(f"Dream: {new_dream.dream_title} was successfully created", 201)

@journal_entry_bp.route("", methods=["GET"], strict_slashes = False)
def get_all_entries():
    journal_entry_response_body = []
    dream_entries = DreamEntry.query.all()
    for entry in dream_entries:
        journal_entry_response_body.append(entry.to_json())
    return jsonify(journal_entry_response_body), 200
    
@journal_entry_bp.route("/<dream_entry_id>", methods=["GET"], strict_slashes = False)
def get_single_entry(dream_entry_id):
    entry = DreamEntry.query.get(dream_entry_id)
    if not entry:
        return "", 404
    return make_response({"Dream entry": entry.to_json()}), 200

@dream_tag_bp.route("", methods=["POST"], strict_slashes = False)
def post_tags():
    request_body = request.get_json()
    new_tag = DreamTag(dream_tag=request_body["dream tag"])

    db.session.add(new_tag)
    db.session.commit()

    return make_response(f"Tag: {new_tag.dream_tag} was successfully created", 201)

@dream_tag_bp.route("", methods=["GET"], strict_slashes = False)
def get_all_tags():
    tag_response_body = []
    tag_entries = DreamTag.query.all()
    for entry in tag_entries:
        tag_response_body.append(entry.to_json())
    return jsonify(tag_response_body), 200

@dream_tag_bp.route("/<tag_id>", methods=["GET"], strict_slashes = False)
def get_single_tag(tag_id):
    tag = DreamTag.query.get(tag_id)
    if not tag:
        return "", 404
    return make_response({"Dream Tag": tag.to_json()}), 200
