from datetime import datetime


def check_if_current(fedtype: str, fedDate: datetime):
  now = datetime.now()

  if fedDate.date() != now.date():
    return False

  if now.hour > 12:
    if fedtype == 'breakfast':
      return False

  return True

def fed_type():
  now = datetime.now()
  if now.hour <= 12:
    return 'breakfast'
  else:
    return 'dinner'
