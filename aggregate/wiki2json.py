import sys
import os
import yaml
import json
from datetime import date, datetime

def json_serial(obj):
  """JSON serializer for objects not serializable by default json code"""

  if isinstance(obj, (datetime, date)):
      return obj.isoformat()
  raise TypeError ("Type %s not serializable" % type(obj))


if __name__ == "__main__":
  basedir = sys.argv[1] + '/_data/devices'
  files = os.listdir(basedir)
  objects = [yaml.load(open(basedir + '/'+ file)) for file in files]

  print(json.dumps(objects, default=json_serial))
