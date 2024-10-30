from flask import Blueprint, request, jsonify
from . import db
from datetime import datetime
from .models import Logdb
import pytz

logApi = Blueprint('log', __name__)

timezone = pytz.timezone('America/New_York')


@logApi.route('/log', methods=['GET'])
def get_status():
  limit = request.args.get('limit', default=None, type=int)
  query_type = request.args.get('type', default=None, type=str)
  query = Logdb.query.order_by(Logdb.timestamp.desc())

  if query_type is not None:
    query = query.filter(Logdb.logtype == query_type)
  if limit is not None:
    query = query.limit(limit)

  feeds = query.all()

  return jsonify([feed.to_dict() for feed in feeds]), 200


@logApi.route('/log', methods=['POST'])
def set_status():
  info = request.json
  log_type = info.get('type')

  if log_type is None:
    return jsonify({'error': 'Missing required field: type'}), 400

  log = Logdb(log_type, datetime.now(timezone))
  db.session.add(log)
  db.session.commit()
  return jsonify({'Added': log.to_dict()}), 200


@logApi.route('/log', methods=['DELETE'])
def delete_status():
  info = request.json
  ids = info.get('id')

  if ids is None:
    return jsonify({'error': 'Missing required field: id'}), 400

  if not isinstance(ids, list):
    return jsonify({'error': 'Field "id" must be a list'}), 400

  if not all(isinstance(item, (int)) and not isinstance(item, bool) for item in ids):
    return jsonify({'error': 'All elements in the list must be an integer'}), 400

  deleted = []
  for id in ids:
    print(id)
    item = Logdb.query.get(id)
    if item:
      db.session.delete(item)
      deleted.append(id)

  db.session.commit()

  return jsonify({'deleted': deleted})
