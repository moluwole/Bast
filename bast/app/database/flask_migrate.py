from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def external():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

