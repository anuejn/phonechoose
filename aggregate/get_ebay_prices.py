from sys import argv, stderr
from get_ebay_price import get_price
from json import dumps, load
from joblib import Parallel, delayed

def add_price(device):
  device["price"] = get_price(device["codename"])
  if device["price"] == -1:
    device["price"] = get_price(device["name"])
  print("%s: %s" % (device["name"], device["price"]), file=stderr)
  return device

if __name__ == "__main__":
  in_obj = load(open(argv[1]))
  out_obj = Parallel(n_jobs=25)(delayed(add_price)(dev) for dev in in_obj)

  print(dumps(out_obj))
