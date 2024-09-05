from datetime import datetime
import pytz

timezone = pytz.timezone('America/New_York')

def check_if_current(fedtype: str, fedDate: datetime):
  fedDate = pytz.utc.localize(fedDate).astimezone(timezone)
  now = datetime.now(timezone)

  if fedDate.date() != now.date():
    return False

  if now.hour > 12:
    if fedtype == 'breakfast':
      return False

  return True

def fed_type():
  now = datetime.now(timezone)
  if now.hour <= 12:
    return 'breakfast'
  else:
    return 'dinner'
