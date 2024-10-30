from flask import Blueprint, request, jsonify
from . import db
from .models import Meddb
from datetime import datetime
import pytz

medApi = Blueprint('med', __name__)

timezone = pytz.timezone('America/New_York')


@medApi.route('/med', methods=['GET'])
def get_status():
  limit = request.args.get('limit', default=None, type=int)
  query_type = request.args.get('type', default=None, type=str)
  query = Meddb.query.order_by(Meddb.timestamp.desc())

  if query_type is not None:
    query = query.filter(Meddb.medtype == query_type)
  if limit is not None:
    query = query.limit(limit)

  feeds = query.all()

  return jsonify([feed.to_dict() for feed in feeds]), 200


@medApi.route('/med', methods=['POST'])
def set_status():
  info = request.json
  med_type = info.get('type')

  if med_type is None:
    return jsonify({'error': 'Missing required field: type'}), 400

  med = Meddb(med_type, datetime.now(timezone))
  db.session.add(med)
  db.session.commit()
  return jsonify({'Added': med.to_dict()}), 200


@medApi.route('/med', methods=['DELETE'])
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
    item = Meddb.query.get(id)
    if item:
      db.session.delete(item)
      deleted.append(id)

  db.session.commit()

  return jsonify({'deleted': deleted})
