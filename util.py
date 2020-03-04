import datetime
import os
from sys import platform

def human_byte_quantity(size, suffix):
  for unit in ['','K','M','G','T','P','E','Z']:
    if abs(size) < 1024.0:
      return "%3.1f %s%s" % (size, unit, suffix)
    size /= 1024.0
  return "%.1f %s%s" % (size, 'Y', suffix)

def eta(downloaded, total, dl_rate):
  if downloaded >= total or dl_rate == 0:
    return ''
  seconds_left = round((total - downloaded) / dl_rate)
  delta = datetime.timedelta(seconds=seconds_left)
  return str(delta)

def get_app_path():
  app_path = os.path.expanduser('~/AppData/Roaming/dtorr' if platform in ('win32', 'cygwin') else '~/.dtorr')
  os.makedirs(app_path, exist_ok=True)
  return app_path
