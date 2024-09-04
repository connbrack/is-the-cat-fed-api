from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db=SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///fed.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  CORS(app)

  from .fed import fedApi
  from .models import Feddb

  app.register_blueprint(fedApi)

  with app.app_context():
      db.create_all()

  return app
