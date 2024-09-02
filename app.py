from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

actual_real_database = {
    'isFed': False,
    'fedDate': None,
}

@app.route('/fed', methods=['GET'])
def get_status():
  isFed = actual_real_database['isFed']

  if isFed == True:
    fedDate = actual_real_database['fedDate']
    isFed = check_time(fedDate)

  return jsonify(actual_real_database)


@app.route('/fed', methods=['POST'])
def set_status():
  isFed = request.json['isFed']
  actual_real_database['isFed'] = isFed
  actual_real_database['fedDate'] = datetime.now()

  return jsonify(actual_real_database), 200


def check_time(fedDate: datetime):
  now = datetime.now()

  if fedDate.date() != now.date():
    return False

  if now.hour > 12:
    if fedDate.hour <= 12:
      return False

  return True


if __name__ == '__main__':
  app.run(debug=True)
