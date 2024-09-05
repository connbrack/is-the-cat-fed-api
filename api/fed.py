from flask import Blueprint, jsonify
from . import db
from .models import Feddb
from datetime import datetime
from .models import Feddb
from .func import check_if_current, fed_type
import pytz

fedApi = Blueprint('data', __name__)

timezone = pytz.timezone('America/New_York')

@fedApi.route('/isfed', methods=['GET'])
def is_fed():
  if Feddb.query.count() != 0:
    lastFed = Feddb.query.order_by(Feddb.id.desc()).first()
    current = check_if_current(lastFed.fedtype, lastFed.timestamp)
    return jsonify({'isFed': current}) 

  return jsonify({'isFed': False}) 


@fedApi.route('/fed', methods=['GET'])
def get_status():
  feeds = Feddb.query.all()
  return jsonify([feed.to_dict() for feed in feeds]), 200


@fedApi.route('/fed', methods=['POST'])
def set_status():

  replaced = False
  if Feddb.query.count() != 0:
    lastFed = Feddb.query.order_by(Feddb.id.desc()).first()
    if check_if_current(lastFed.fedtype, lastFed.timestamp):
      db.session.delete(lastFed)
      db.session.commit()
      replaced = True

  fed = Feddb(fed_type(), datetime.now(timezone))
  db.session.add(fed)
  db.session.commit()
  return jsonify({'Added': fed.to_dict(), 'replaced': replaced}), 200


@fedApi.route('/fed', methods=['DELETE'])
def delete_status():
  if Feddb.query.count() != 0:
    lastFed = Feddb.query.order_by(Feddb.id.desc()).first()
    if check_if_current(lastFed.fedtype, lastFed.timestamp):
      db.session.delete(lastFed)
      db.session.commit()
      return jsonify({'deleted': lastFed.to_dict()})
    
  return jsonify({'deleted': 'none'})

