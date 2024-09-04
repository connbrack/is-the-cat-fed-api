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


print()
