import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()
dbURL = str(os.getenv('dbURL'))


def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = dbURL
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  CORS(app)

  from .fed import fedApi
  from .med import medApi
  from .log import logApi
  from .models import Feddb, Meddb, Logdb

  app.register_blueprint(fedApi)
  app.register_blueprint(medApi)
  app.register_blueprint(logApi)

  with app.app_context():
    db.create_all()

  return app
