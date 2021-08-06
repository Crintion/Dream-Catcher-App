from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/mood_catcher_db_development'


    # Import models here for Alembic setup
    from app.models.journal_entry import JournalEntry
    from app.models.journal_tag import JournalTag
    from app.routes import journal_tag_bp
    from app.routes import journal_entry_bp


    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(journal_entry_bp)
    app.register_blueprint(journal_tag_bp)

    return app
