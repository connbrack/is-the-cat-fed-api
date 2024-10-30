from . import db


class Feddb(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fedtype = db.Column(db.String)
  timestamp = db.Column(db.DateTime)

  def __init__(self, fedtype, timestamp):
    self.fedtype = fedtype
    self.timestamp = timestamp

  def __repr__(self):
    return f"fedtype: {self.fedtype}, timestamp: {self.timestamp}"

  def to_dict(self):
    return {
        "id": self.id,
        "fedtype": self.fedtype,
        "timestamp": self.timestamp,
    }


class Meddb(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  medtype = db.Column(db.String)
  timestamp = db.Column(db.DateTime)

  def __init__(self, medtype, timestamp):
    self.medtype = medtype
    self.timestamp = timestamp

  def __repr__(self):
    return f"medtype: {self.medtype}, timestamp: {self.timestamp}"

  def to_dict(self):
    return {
        "id": self.id,
        "medtype": self.medtype,
        "timestamp": self.timestamp,
    }


class Logdb(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  logtype = db.Column(db.String)
  timestamp = db.Column(db.DateTime)

  def __init__(self, logtype, timestamp):
    self.logtype = logtype
    self.timestamp = timestamp

  def __repr__(self):
    return f"logtype: {self.logtype}, timestamp: {self.timestamp}"

  def to_dict(self):
    return {
        "id": self.id,
        "logtype": self.logtype,
        "timestamp": self.timestamp,
    }
